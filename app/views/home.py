from flask import Blueprint, request, render_template, g, \
                  flash, session, redirect, url_for
# from flask.ext.login import login_required

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.forms import LoginForm, RegisterForm
from app.models import Student, Donor


home = Blueprint('home', __name__, 
    template_folder='templates/home', static_folder='static')


@home.route('/')
@home.route('/index')
def index():
    return render_template("home/index.html")

# pull user's profile from the database before every request are treated
@home.before_request
def before_request():
    g.user = None
    if 'student_id' in session:
        g.user = Student.query.get(session['student_id'])
    if 'donor_id' in session:
        g.user = Student.query.get(session['donor_id'])

# Set the route and accepted methods
@home.route('/login', methods=['GET', 'POST'])
def login():
    # If sign in form is submitted
    form = LoginForm(request.form)
    if form.validate_on_submit():
        if form.user_type.data == 1: # student
            user = Student.query.filter_by(email=form.email.data).first()
            user_id = 'student_id'
        elif form.user_type.data == 2: # donor
            user = Donor.query.filter_by(email=form.email.data).first()
            user_id = 'donor_id'
        if user and check_password_hash(user.password, form.password.data):
            session[user_id] = user.id
            flash('Welcome %s' % user.first_name)
            return redirect(url_for('home.index'))

        flash('Wrong email or password', 'error-message')
    return render_template("home/login.html", form=form)

@home.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        if form.user_type.data == 1:
            user = Student(first_name=form.first_name.data, last_name=form.last_name.data,
                email=form.email.data, password=generate_password_hash(form.password.data))
            user_id = 'student_id'
        elif form.user_type.data == 2:
            user = Donor(first_name=form.first_name.data, last_name=form.last_name.data,
                email=form.email.data, password=generate_password_hash(form.password.data))
            user_id = 'donor_id'

        db.session.add(user)
        db.session.commit()
        session[user_id] = user.id
        flash('Thanks for registering')
        return redirect(url_for('home.index'))
    return render_template("home/register.html", form=form)


@home.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home.index'))



