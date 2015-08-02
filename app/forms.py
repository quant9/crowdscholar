from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, RadioField, \
    SelectField, IntegerField
# from wtforms fmport RecaptchaField

from wtforms.validators import InputRequired, Email, EqualTo, Length, Optional, Regexp
from . import constants

message = 'Field is required.'

class RegisterForm(Form):
    user_type = RadioField('Student or Donor?', [InputRequired(message=message)],
        choices=[(1, 'Student'), (2, 'Donor')], default=1, coerce=int)
    first_name = StringField('First Name', [InputRequired(message=message)])
    last_name = StringField('Last Name', [InputRequired(message=message)])
    email = StringField('Email Address', [InputRequired(message=message), Email()])
    password = PasswordField('Password', [InputRequired(message=message)])
    confirm = PasswordField('Repeat Password', [
        InputRequired(message=message),
        EqualTo('password', message='Passwords must match')])
    accept_tos = BooleanField('I accept the TOS', [InputRequired(message=message)])
    # recaptcha = RecaptchaField()

class LoginForm(Form):
    user_type = RadioField('User Type', [InputRequired(message=message)],
        choices=[(1, 'Student'), (2, 'Donor')], default=1, coerce=int)
    email = StringField('Email Address', [InputRequired(message=message), Email()])
    password = PasswordField('Password', [InputRequired(message=message)])

class ChangePasswordForm(Form):
    password = PasswordField('New Password', [
                InputRequired(message=message),
                EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [InputRequired(message=message)])


class ApplicationForm(Form):
    pass

class CreateCampaignForm(Form):
    pass

class DonationForm(Form):
    pass

class CreateScholarshipForm(Form):
    pass

class ProfileForm(Form):
    gender = SelectField('Gender', [InputRequired(message=message)],
        choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], coerce=int)
    # TODO: check valid addresses
    address = StringField('Street Address', [InputRequired(message=message),
        Regexp('^\d'), Length(max=300)])
    apt_no = StringField('Apartment # (optional)', [Length(max=5), Optional()])
    city = StringField('City', [InputRequired(message=message), Length(max=100)])
    state = SelectField('State (United States only)', choices=constants.STATES)
    zipcode = StringField('Zip Code (5-digit)', 
        [Regexp('\d{5}', message='Not a valid zip code.')])

class StudentProfileForm(ProfileForm):
    pass

class DonorProfileForm(ProfileForm):
    alma_mater = StringField('Alma Mater', [Optional(), Length(max=100)])
    profession = StringField('Profession', [Optional(), Length(max=100)])
    company = StringField('Company', [Optional(), Length(max=200)])
    bio = TextAreaField('Tell us about yourself (500 characters)', [Optional(), Length(max=500)])

