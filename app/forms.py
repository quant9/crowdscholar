from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, RadioField, \
    SelectField, IntegerField, SelectMultipleField
# from wtforms fmport RecaptchaField

from wtforms.validators import Required, InputRequired, Email, EqualTo, Length, Optional, Regexp
from . import constants

message = 'Field is required.'


# a validator which makes a field required if another field is set and has a truthy value
class RequiredIf(Required):

    def __init__(self, other_field_name, *args, **kwargs):
        self.other_field_name = other_field_name
        super(RequiredIf, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        if other_field.data == 0:
            super(RequiredIf, self).__call__(form, field)


class RegisterForm(Form):
    user_type = RadioField('Student or Donor?', [InputRequired(message=message)],
        choices=[(1, 'Student'), (2, 'Donor')], default=1, coerce=int)
    first_name = StringField('First / given name', [InputRequired(message=message)])
    last_name = StringField('Last name (family name / surname)', [InputRequired(message=message)])
    email = StringField('Email Address', [InputRequired(message=message), Email()])
    password = PasswordField('Password', [InputRequired(message=message)])
    confirm = PasswordField('Repeat Password', [
        InputRequired(message=message), EqualTo('password', message='Passwords must match')])
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
    amount = RadioField('Amount', [InputRequired(message=message)],
        choices=[(10, '$10'), (50, '$50'), (100, '$100'), (250, '$250'), (500, '$500'), (0, 'Other amount')],
        default = 50, coerce=int)
    other_amount = IntegerField('Other amount: ($1 increments)', 
        [RequiredIf('amount', message=message)], default=0)
    message = TextAreaField('Send a message to the scholarship creator: (optional)', [Optional()])


class FilterForm(Form):
    category = SelectMultipleField('Select category', choices=constants.CATEGORIES, coerce=int)
    affiliation = SelectMultipleField('Select affiliation', choices=constants.AFFILIATIONS, coerce=int)


class CreateScholarshipForm(Form):
    name = StringField('Scholarship name', [InputRequired(message=message)])
    category = SelectField('Select category', choices=constants.CATEGORIES)
    affiliation = SelectField('Select affiliation', choices=constants.AFFILIATIONS)
    grade_9 = BooleanField('9th')
    grade_10 = BooleanField('10th')
    grade_11 = BooleanField('11th')
    grade_12 = BooleanField('12th')
    undergrad_not_enrolled = BooleanField('High School graduate not enrolled in college')
    undergrad_enrolled = BooleanField('Current college student')
    postgrad_not_enrolled = BooleanField('Prospective graduate student')
    postgrad_enrolled = BooleanField('Current graduate student')
    slug = TextAreaField('Brief description', [InputRequired(message=message)])
    amount_target = IntegerField('Other amount: ($1 increments)', 
        [InputRequired(message=message)], default=2500)
    description = TextAreaField('Extended description', [InputRequired(message=message)])


class ProfileForm(Form):
    gender = SelectField('Gender', [InputRequired(message=message)],
        choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], coerce=int)
    address = StringField('Street Address', [InputRequired(message=message),
        Regexp('^\d'), Length(max=300)])
    apt_no = StringField('Apartment # (optional)', [Length(max=5), Optional()])
    city = StringField('City', [InputRequired(message=message), Length(max=100)])
    state = SelectField('State (United States only)', choices=constants.STATES)
    zipcode = StringField('Zip Code (5-digit)', 
        [Regexp('\d{5}', message='Not a valid zip code.')])
    phone = StringField('Phone number', [InputRequired(message=message), Length(max=20),
        Regexp('^[0-9(]+.+\d$')])

class StudentProfileForm(ProfileForm):
    pass


class DonorProfileForm(ProfileForm):
    alma_mater = StringField('Alma Mater', [Optional(), Length(max=100)])
    profession = StringField('Profession', [Optional(), Length(max=100)])
    company = StringField('Company', [Optional(), Length(max=200)])
    bio = TextAreaField('Tell us about yourself (1000 characters max)', 
        [Optional(), Length(max=1000)])


