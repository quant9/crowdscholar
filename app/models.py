from app import db
from app import constants
from flask.ext.login import UserMixin
import datetime

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

class Student(User):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Campaign(db.Model):
    __tablename__ = 'campaigns'
    campaign_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))


class Donor(User):
    __tablename__ = 'donors'
    donor_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gender = db.Column(db.SmallInteger, nullable=True)
    address = db.Column(db.String(300), nullable=True)
    apt_no = db.Column(db.String(10), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(10), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    alma_mater = db.Column(db.String(100), nullable=True)
    profession = db.Column(db.String(100), nullable=True)
    company = db.Column(db.String(200), nullable=True)

class Scholarship(db.Model):
    __tablename__ = 'scholarships'
    scholarship_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('donors.donor_id'))
    name = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.Text, nullable=False)
    amount_target = db.Column(db.Float, nullable=False)
    amount_funded = db.Column(db.Float, default=0)
    status = db.Column(db.Integer, default=constants.FUNDING)
    description = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    expiration_date = db.Column(db.DateTime,
        default=datetime.datetime(2099,12,31))

    def __init__(self, creator_id, name, slug, target_amount, 
        description=None, expiration_date=None):
        self.creator_id = creator_id
        self.name = name
        self.slug = slug
        self.target_amount = target_amount
        self.description = description
        self.expiration_date = expiration_date

class Donation(db.Model):
    __tablename__ = 'donations'
    donation_id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('donors.donor_id'))
    scholarship_id = db.Column(db.Integer, db.ForeignKey('donors.donor_id'))
    amount = db.Column(db.Float, nullable=False)
    cleared = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, donor_id, scholarship_id, amount, cleared=False):
        self.donor_id = donor_id
        self.scholarship_id = scholarship_id
        self.amount = amount
        self.cleared = cleared








