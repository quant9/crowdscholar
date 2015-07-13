from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, RadioField
# from wtforms fmport RecaptchaField

from wtforms.validators import InputRequired, Email, EqualTo

message = 'Field is required.'

class RegisterForm(Form):
    user_type = RadioField('Student or Donor?', [InputRequired(message=message)],
        choices=[(1, 'Student'), (2, 'Donor')], default=1)
    first_name = TextField('First Name', [InputRequired(message=message)])
    last_name = TextField('Last Name', [InputRequired(message=message)])    
    email = TextField('Email Address', [InputRequired(message=message), Email()])
    password = PasswordField('Password', [InputRequired(message=message)])
    confirm = PasswordField('Repeat Password', [
        InputRequired(message=message),
        EqualTo('password', message='Passwords must match')])
    accept_tos = BooleanField('I accept the TOS', [InputRequired(message=message)])
    # recaptcha = RecaptchaField()

class LoginForm(Form):
    user_type = RadioField('User Type', [InputRequired(message=message)],
        choices=[(1, 'Student'), (2, 'Donor')], default=1)
    email = TextField('Email Address', [InputRequired(message=message), Email()])
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
    pass

class StudentProfileForm(ProfileForm):
    pass

class DonorProfileForm(ProfileForm):
    pass
