from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask.ext.login import login_user, logout_user, current_user
from app import db, login_manager
from app.forms import CreateScholarshipForm, DonationForm, DonorProfileForm
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
        if scholarship:
            return render_template('donor/browse.html', scholarship=scholarship)
    full_list = Scholarship.query.join(Donor).____
    return render_template('donor/browse.html', full_list=full_list)


@donor.route('/profile')
@donor.route('/<donor_id>')
@login_required(user_type=2)
def profile(donor_id=None):
    if donor_id:
        donor = Donor.query.filter_by(donor_id=donor_id).first()
        return render_template('profile.html', donor=donor)
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


@donor.route('/update', methods=['GET', 'POST'])
@login_required(user_type=2)
def update():
    form = DonorProfileForm()
    if form.validate_on_submit():
        donor = Donor.query.get()
        form.populate_obj(user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('update'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('update.html', form=form, title="Crowdscholar: update profile")



# https://exploreflask.com/blueprints.html
# @donor.url_value_preprocessor
# def get_profile_owner(endpoint, values):
#     query = Donor.query.filter_by(url_slug=values.pop('donor_id'))
#     g.profile_owner = query.first_or_404()
