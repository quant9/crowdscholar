from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, RadioField, \
    SelectField
# from wtforms fmport RecaptchaField

from wtforms.validators import InputRequired, Email, EqualTo, Length

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
    pass

class StudentProfileForm(ProfileForm):
    pass

class DonorProfileForm(ProfileForm):
    nickname = StringField('nickname', validators=[InputRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
    gender = SelectField('Gender', choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], 
        coerce=int, [InputRequired(message=message)])
    address = 
    city = db.Column(db.String(100))
    state = db.Column(db.String(10))
    alma_mater = db.Column(db.String(100))
    profession = db.Column(db.String(100))
    company = db.Column(db.String(200))


    gender = db.Column(db.SmallInteger)
    address = db.Column(db.String(300))
    city = db.Column(db.String(100))
    state = db.Column(db.String(10))
    alma_mater = db.Column(db.String(100))
    profession = db.Column(db.String(100))
    company = db.Column(db.String(200))
















