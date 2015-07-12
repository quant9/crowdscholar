# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField, BooleanField RecaptchaField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo

message = 'Field is required.'

class RegisterForm(Form):
    first_name = TextField('First Name', [Required(message=message)])
    last_name = TextField('Last Name', [Required(message=message)])    
    email = TextField('Email Address', [Required(message=message), Email()])
    password = PasswordField('Password', [Required(message=message)])
    confirm = PasswordField('Repeat Password', [
        Required(message=message),
        EqualTo('password', message='Passwords must match')])
    accept_tos = BooleanField('I accept the TOS', [Required(message=message)])
    recaptcha = RecaptchaField()

class LoginForm(Form):
    email = TextField('Email Address', [Required(message=message), Email()])
    password = PasswordField('Password', [Required(message=message)])

class ChangePasswordForm(Form):
    password = PasswordField('New Password', [
                Required(message=message),
                EqualTo('confirm', mesage='Passwords must match')])
    confirm = PasswordField('Repeat Password', [Required(message=message)])
