from flask import Blueprint, render_template, g
from ..models import Donor

donor_profile = Blueprint('donor_profile', __name__,
                    template_folder='templates',
                    static_folder='static')


@donor_profile.route('/<donor_id>/create')
def create(user_url_slug):
    return render_template('donor/create.html')


@donor_profile.route('/<donor_id>/donate')
def donate(user_url_slug):
    return render_template('donor/donate.html')


@donor_profile.route('/<donor_id>')
@donor_profile.route('/<donor_id>/profile')
def profile(user_url_slug):
    return render_template('donor/profile.html')


@donor_profile.route('/<donor_id>/update')
def update(user_url_slug):
    return render_template('donor/update.html')


# https://exploreflask.com/blueprints.html
@donor_profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Donor.query.filter_by(url_slug=values.pop('donor_id'))
    g.profile_owner = query.first_or_404()
