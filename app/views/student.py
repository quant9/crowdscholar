from flask import Blueprint, render_template, g
from ..models import Student

student_profile = Blueprint('student_profile', __name__,
                    template_folder='templates',
                    static_folder='static')


@student_profile.route('/<student_id>')
def profile(user_url_slug):
    return render_template('student/profile.html')


@student_profile.route('/<student_id>/applications')
def applications(user_url_slug):
    return render_template('student/applications.html')


@student_profile.route('/<student_id>/update')
def update(user_url_slug):
    return render_template('student/update.html')


# https://exploreflask.com/blueprints.html
@student_profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Student.query.filter_by(url_slug=values.pop('student_id'))
    g.profile_owner = query.first_or_404()
