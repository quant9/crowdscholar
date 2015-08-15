from flask import Blueprint, request, render_template, \
                  flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user
from functools import wraps

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

from app import db, login_manager
from app.forms import LoginForm, RegisterForm
from app.models import User, Student, Donor
from app.oauth import OAuthSignIn
from sqlalchemy.exc import IntegrityError

home = Blueprint('home', __name__, 
    template_folder='templates/home', static_folder='static')

# custom login_required function to support different user_types
def login_required(user_type=0):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            elif (current_user.user_type != user_type) and (user_type != 0):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# necessary for flask login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    flash('You are not authorized to view the requested page.')
    return redirect(url_for('home.index'))

@home.route('/')
@home.route('/index')
def index():
    return render_template("home/index.html")

@home.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('home.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@home.route('/callback/<provider>')
def oauth_callback(provider, user_type=1):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    email, first_name, last_name = oauth.callback()
    if email is None:
        flash('Facebook authentication failed. Try again or register via email.')
        return redirect(url_for('home.register'))
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(first_name=first_name, last_name=last_name,
            email=email, password='', user_type=1)
        db.session.add(user)
        if user_type == 1:
            student = Student(user_id=User.query.filter_by(email=email).first().id)
            db.session.add(student)
        if user_type == 2:
            donor = Donor(user_id=User.query.filter_by(email=email).first().id)
            db.session.add(donor)
        db.session.commit()
    login_user(user, remember=False)
    return redirect(url_for('home.index'))

@home.route('/login', methods=['GET', 'POST'])
def login():
    # if already signed in take to homepage
    if current_user.is_authenticated():
        return redirect(url_for('home.index'))

    # If sign in form is submitted
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.user_type == form.user_type.data:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=False) # TODO: add remember me
                flash('Welcome, %s!' % user.first_name)
                return redirect(url_for('home.index'))

        flash('Wrong email or password', 'error-message')
    return render_template("home/login.html", form=form)

@home.route('/register', methods=['GET', 'POST'])
def register():
    # if already signed in take to homepage
    if current_user.is_authenticated():
        return redirect(url_for('home.index'))

    form = RegisterForm(request.form)
    if form.validate_on_submit():
        if form.user_type.data == 1:
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                email=form.email.data, password=generate_password_hash(form.password.data),
                user_type=1)
        elif form.user_type.data == 2:
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                email=form.email.data, password=generate_password_hash(form.password.data),
                user_type=2)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            flash('An account with this email already exists.')
        else:
            if form.user_type.data == 1:
                student = Student(user_id=User.query.filter_by(email=form.email.data).first().id)
                db.session.add(student)
            elif form.user_type.data == 2:
                donor = Donor(user_id=User.query.filter_by(email=form.email.data).first().id)
                db.session.add(donor)
            db.session.commit()
            login_user(user, remember=False) # TODO: add remember me
            flash('Thanks for registering')
            return redirect(url_for('home.index'))

    return render_template("home/register.html", form=form)


@home.route('/logout')
def logout():
    logout_user()
    # session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home.index'))

