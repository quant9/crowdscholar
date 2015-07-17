from app import db
from app import constants
from flask.ext.login import UserMixin

# base models for other tables to inherit
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    user_type = db.Column(db.SmallInteger, default=constants.OTHERUSER)
    status = db.Column(db.SmallInteger, default=constants.NEW)

    def __init__(self, first_name, last_name, email, password, user_type):
        self.first_name  = first_name
        self.last_name  = last_name
        self.email = email
        self.password = password
        self.user_type = user_type

    def get_status(self):
        return constants.STATUS[self.status]

    def get_user_type(self):
        return constants.USERTYPE[self.user_type]

    @classmethod
    def get_user(cls, id):
        pass

    def __repr__(self):
        return '<User %r>' % (self.first_name)

# Define a Student model
class Student(User):
    __tablename__ = 'students'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    student_id = db.Column(db.Integer, primary_key=True)

# Define a Student model
class Donor(User):
    __tablename__ = 'donors'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    donor_id = db.Column(db.Integer, primary_key=True)
