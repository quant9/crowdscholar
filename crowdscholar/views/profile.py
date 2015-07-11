
from flask import Blueprint, render_template

student_profile = Blueprint('student_profile', __name__,
                    template_folder='templates',
                    static_folder='static')

@student_profile.route('/<student_id>')
def profile(user_url_slug):
    # Do some stuff
    return render_template('student_profile/profile.html')

@student_profile.route('/<student_id>/applications')
def applications(user_url_slug):
    # Do some stuff
    return render_template('student_profile/applications.html')

@student_profile.route('/<student_id>/update')
def update(user_url_slug):
    # Do some stuff
    return render_template('student_profile/update.html')


donor_profile = Blueprint('donor_profile', __name__,
                    template_folder='templates',
                    static_folder='static')

