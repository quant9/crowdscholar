from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask.ext.login import login_user, logout_user, current_user
from app import login_manager
from app.forms import CreateScholarshipForm, DonationForm
from app.models import Donor, Scholarship, Campaign, Donation
from .home import login_required

donor = Blueprint('donor', __name__, url_prefix='/donor',
    template_folder='templates/donor', static_folder='static')


@donor.route('/browse')
@donor.route('/browse/<int:scholarship_id>')
@login_required(user_type=2)
def browse(scholarship_id=None):
    if scholarship_id:
        scholarship = Scholarship.query.join(Donor).filter(Scholarship.scholarship_id==scholarship_id).first() or None
        return render_template('donor/browse.html', scholarship=scholarship)
    # elif campaign_id:
    #     c = Campaign.query.filter_by(campaign_id=campaign_id).first() or None
    #     return render_template('donor/browse.html', campaign=c)
    else:
        return render_template('donor/browse.html')


@donor.route('/profile')
@donor.route('/<donor_id>')
@login_required(user_type=2)
def profile(donor_id):
    return render_template('profile.html')


@donor.route('/create', methods=['GET', 'POST'])
@login_required(user_type=2)
def create(donor_id):
    form = CreateScholarshipForm(request.form)
    if form.validate_on_submit():
        flash('scholarship was successfully created!')
        return redirect(url_for('home.index'))
    return render_template('create.html')


@donor.route('/<int:scholarship_id>/donate')
@login_required(user_type=2)
def donate(scholarship_id):
    form = DonationForm(request.form)
    if form.validate_on_submit():
        pass
    return render_template('donate.html', form=form, scholarship_id=scholarship_id)


@donor.route('/update')
@login_required(user_type=2)
def update(donor_id):
    return render_template('update.html')


# https://exploreflask.com/blueprints.html
# @donor.url_value_preprocessor
# def get_profile_owner(endpoint, values):
#     query = Donor.query.filter_by(url_slug=values.pop('donor_id'))
#     g.profile_owner = query.first_or_404()
