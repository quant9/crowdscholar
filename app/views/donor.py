from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask.ext.login import login_user, logout_user, current_user
from app import login_manager
from ..models import Donor
from .home import login_required

donor_profile = Blueprint('donor_profile', __name__, url_prefix='/donor',
    template_folder='templates/donor', static_folder='static')


@donor_profile.route('/<donor_id>')
@donor_profile.route('/<donor_id>/profile')
@login_required(user_type='donor')
def profile(donor_id):
    return render_template('profile.html')


@donor_profile.route('/<donor_id>/create', methods=['GET', 'POST'])
@login_required(user_type='donor')
def create(donor_id):
    if request.method == 'POST':
        flash('scholarship was successfully created!')
        return redirect(url_for('home.index'))
    return render_template('create.html')


@donor_profile.route('/<donor_id>/donate')
@login_required(user_type='donor')
def donate(donor_id):
    return render_template('donate.html')


@donor_profile.route('/<donor_id>/update')
@login_required(user_type='donor')
def update(donor_id):
    return render_template('update.html')


# https://exploreflask.com/blueprints.html
@donor_profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Donor.query.filter_by(url_slug=values.pop('donor_id'))
    g.profile_owner = query.first_or_404()
