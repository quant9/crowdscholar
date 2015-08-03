from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from flask.ext.login import current_user
from app import db, login_manager
from app.forms import CreateScholarshipForm, DonationForm, DonorProfileForm
from app.models import User, Donor, Scholarship, Campaign, Donation
from .home import login_required

donor = Blueprint('donor', __name__, url_prefix='/donor',
    template_folder='templates/donor', static_folder='static')


@donor.route('/browse/')
@donor.route('/browse/<int:scholarship_id>')
@login_required(user_type=2)
def browse(scholarship_id=None):
    if scholarship_id:
        scholarship = Scholarship.get_scholarship(scholarship_id)
        if scholarship:
            return render_template('donor/browse.html', scholarship=scholarship)
        flash("The scholarship you requested is unavailable. \
            Browse all scholarships below.".format(scholarship_id))
    full_list = Scholarship.query.all()
    return render_template('donor/browse.html', full_list=full_list)


@donor.route('/profile/')
@donor.route('/profile/<int:donor_id>')
@login_required(user_type=2)
def profile(user_id=None, donor_id=None):
    if donor_id:
        donor = Donor.get_donor(donor_id=donor_id)
        if donor:
            return render_template('donor/profile.html', donor=donor)
        flash("The donor profile you selected is unavailable. \
            We've redirected you to your own profile.".format(donor_id))
    donor = Donor.query.filter_by(user_id=current_user.id).first() or None
    return render_template('donor/profile.html', donor=donor)


@donor.route('/create', methods=['GET', 'POST'])
@login_required(user_type=2)
def create(donor_id):
    form = CreateScholarshipForm(request.form)
    if form.validate_on_submit():
        flash('scholarship was successfully created!')
        return redirect(url_for('home.index'))
    return render_template('donor/create.html')


@donor.route('/donate/')
@donor.route('/donate/<int:scholarship_id>', methods=['GET', 'POST'])
@login_required(user_type=2)
def donate(scholarship_id=None):
    scholarship = Scholarship.get_scholarship(scholarship_id)
    if not scholarship:
        flash('Error finding donation page. Please make sure the scholarship ID is correct.')
        return redirect(url_for('donor.browse'))

    form = DonationForm(request.form)
    if form.validate_on_submit():
        amount = form.amount.data or form.other_amount.data
        donation = Donation(donor_id=Donor.get_donor(user_id=current_user.id).donor_id, 
            scholarship_id=scholarship_id, message=form.message.data,
            amount=amount, cleared=False)
        db.session.add(donation)
        db.session.commit()
        flash('Thank you for your donation!')
        return render_template('donor/success.html', scholarship=scholarship, donation=donation)

    return render_template('donor/donate.html', form=form, scholarship=scholarship)


@donor.route('/update', methods=['GET', 'POST'])
@login_required(user_type=2)
def update():
    donor = Donor.query.filter_by(user_id=current_user.id).first() or None
    if donor:
        form = DonorProfileForm(request.form, obj=donor)
        if form.validate_on_submit():
            form.populate_obj(donor)
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('donor.profile'))
        return render_template('donor/update.html', form=form)
    flash('Your donor information could not be retrieved. We apologize for the inconvenience.')
    return redirect(url_for('donor.profile'))


# https://exploreflask.com/blueprints.html
# @donor.url_value_preprocessor
# def get_profile_owner(endpoint, values):
#     query = Donor.query.filter_by(url_slug=values.pop('donor_id'))
#     g.profile_owner = query.first_or_404()
