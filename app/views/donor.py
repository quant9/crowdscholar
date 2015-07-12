from flask import Blueprint, render_template, g
from flask.ext.login import login_required
from ..models import Donor

donor_profile = Blueprint('donor_profile', __name__,
                    template_folder='templates',
                    static_folder='static')


@donor_profile.route('/<donor_id>')
@donor_profile.route('/<donor_id>/profile')
@login_required
def profile(donor_id):
    return render_template('donor/profile.html')


@donor_profile.route('/<donor_id>/create')
@login_required
def create(donor_id):
    return render_template('donor/create.html')


@donor_profile.route('/<donor_id>/donate')
@login_required
def donate(donor_id):
    return render_template('donor/donate.html')


@donor_profile.route('/<donor_id>/update')
@login_required
def update(donor_id):
    return render_template('donor/update.html')


# https://exploreflask.com/blueprints.html
@donor_profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Donor.query.filter_by(url_slug=values.pop('donor_id'))
    g.profile_owner = query.first_or_404()
