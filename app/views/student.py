from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask.ext.login import login_user, logout_user, current_user
from app import login_manager
from ..models import Student
from .home import login_required


student = Blueprint('student', __name__, url_prefix='/student',
    template_folder='templates/student', static_folder='static')


@student.route('/browse')
@student.route('/browse/<int:scholarship_id>')
@student.route('/browse/<int:campaign_id>')
@login_required(user_type='student')
def browse(scholarship_id=None, campaign_id=None):
    if scholarship_id:
        return render_template('student/browse.html', scholarship_id=scholarship_id)
    elif campaign_id:
        return render_template('student/browse.html', campaign_id=campaign_id)
    else:
        return render_template('student/browse.html')


@student.route('/profile')
@student.route('/<student_id>')
@login_required(user_type='student')
def profile(student_id):
    return render_template('profile.html', student_id=student_id)


@student.route('/apply')
@login_required(user_type='student')
def apply(student_id):
    return render_template('apply.html')


@student.route('/create', methods=['GET', 'POST'])
@login_required(user_type='student')
def create(student_id):
    if request.method == 'POST':
        flash('Your campaign was successfully created!')
        return redirect(url_for('home.index'))
    return render_template('create.html')


@student.route('/update')
@login_required(user_type='student')
def update(student_id):
    return render_template('update.html')


# https://exploreflask.com/blueprints.html
@student.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Student.query.filter_by(url_slug=values.pop('student_id'))
    g.profile_owner = query.first_or_404()
