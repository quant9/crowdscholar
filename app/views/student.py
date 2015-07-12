from flask import Blueprint, render_template, g
from flask.ext.login import login_required
from ..models import Student

student_profile = Blueprint('student_profile', __name__, url_prefix='/student',
    template_folder='templates/student', static_folder='static')


@student_profile.route('/<student_id>')
@student_profile.route('/<student_id>/profile')
@login_required
def profile(student_id):
    return render_template('profile.html')


@student_profile.route('/<student_id>/apply')
@login_required
def apply(student_id):
    return render_template('apply.html')


@student_profile.route('/<student_id>/create')
@login_required
def create(student_id):
    return render_template('create.html')


@student_profile.route('/<student_id>/update')
@login_required
def update(student_id):
    return render_template('update.html')


# https://exploreflask.com/blueprints.html
@student_profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Student.query.filter_by(url_slug=values.pop('student_id'))
    g.profile_owner = query.first_or_404()
