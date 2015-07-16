from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from ..models import Student
from app import login_manager


student_profile = Blueprint('student_profile', __name__, url_prefix='/student',
    template_folder='templates/student', static_folder='static')


@student_profile.route('/<student_id>')
@student_profile.route('/<student_id>/profile')
@login_required(user_type='student')
def profile(student_id):
    return render_template('profile.html')


@student_profile.route('/<student_id>/apply')
@login_required(user_type='student')
def apply(student_id):
    return render_template('apply.html')


@student_profile.route('/<student_id>/create')
@login_required(user_type='student')
def create(student_id):
    if request.method == 'POST':
        flash('scholarship was successfully created!')
        return redirect(url_for('home.index'))
    return render_template('create.html')

@student_profile.route('/<student_id>/update')
@login_required(user_type='student')
def update(student_id):
    return render_template('update.html')


# https://exploreflask.com/blueprints.html
@student_profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Student.query.filter_by(url_slug=values.pop('student_id'))
    g.profile_owner = query.first_or_404()
