from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask.ext.login import login_user, logout_user, current_user
from app import login_manager
from app.forms import CreateScholarshipForm, DonationForm
from ..models import Donor
from .home import login_required

donor = Blueprint('donor', __name__, url_prefix='/donor',
    template_folder='templates/donor', static_folder='static')


@donor.route('/browse')
@donor.route('/browse/<int:scholarship_id>')
@donor.route('/browse/<int:campaign_id>')
@login_required(user_type='donor')
def browse(scholarship_id=None, campaign_id=None):
    if scholarship_id:
        return render_template('donor/browse.html', scholarship_id=scholarship_id)
    elif campaign_id:
        return render_template('donor/browse.html', campaign_id=campaign_id)
    else:
        return render_template('donor/browse.html')


@donor.route('/profile')
@donor.route('/<donor_id>')
@login_required(user_type='donor')
def profile(donor_id):
    return render_template('profile.html')


@donor.route('/create', methods=['GET', 'POST'])
@login_required(user_type='donor')
def create(donor_id):
    form = CreateScholarshipForm(request.form)
    if form.validate_on_submit():
        flash('scholarship was successfully created!')
        return redirect(url_for('home.index'))
    return render_template('create.html')


@donor.route('/<int:scholarship_id>/donate')
@login_required(user_type='donor')
def donate(scholarship_id):
    form = DonationForm(request.form)
    if form.validate_on_submit():
        pass
    return render_template('donate.html', form=form, scholarship_id=scholarship_id)


@donor.route('/update')
@login_required(user_type='donor')
def update(donor_id):
    return render_template('update.html')


# https://exploreflask.com/blueprints.html
@donor.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = Donor.query.filter_by(url_slug=values.pop('donor_id'))
    g.profile_owner = query.first_or_404()
