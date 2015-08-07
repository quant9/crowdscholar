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
    is_student = db.relationship('Student', backref='users', lazy='dynamic')
    is_donor = db.relationship('Donor', backref='users', lazy='dynamic')

    def get_status(self):
        return constants.STATUS[self.status]

    def get_user_type(self):
        return constants.USERTYPE[self.user_type]

    @classmethod
    def get_user(cls, id):
        pass

    def __repr__(self):
        return '<User %r>' % (self.first_name)

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Campaign(db.Model):
    __tablename__ = 'campaigns'
    campaign_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))


class Donor(db.Model):
    __tablename__ = 'donors'
    donor_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gender = db.Column(db.SmallInteger, nullable=True)
    address = db.Column(db.String(300), nullable=True)
    apt_no = db.Column(db.String(10), nullable=True)
    # phone_no = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(10), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    alma_mater = db.Column(db.String(100), nullable=True)
    profession = db.Column(db.String(100), nullable=True)
    company = db.Column(db.String(200), nullable=True)
    bio = db.Column(db.Text(500), default="I'm proud to be a donor on Crowdscholar!")
    scholarships_created = db.relationship('Scholarship', backref='donors', lazy='dynamic')
    donations = db.relationship('Donation', backref='donors', lazy='dynamic')

    @classmethod
    def get_donor(cls, user_id=None, donor_id=None):
        if user_id:
            return Donor.query.filter_by(user_id=user_id).first()
        if donor_id:
            return Donor.query.filter_by(donor_id=donor_id).first()
        return None

    def get_user(self):
        return User.query.filter_by(id=self.user_id).first()


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
    expiration_date = db.Column(db.DateTime, default=datetime.datetime(2099,12,31))
    donations_to = db.relationship('Donation', backref='scholarships', lazy='dynamic')

    @classmethod
    def get_scholarship(cls, s_id):
        return Scholarship.query.join(Donor).filter(Scholarship.scholarship_id == s_id).first()

    def get_creator(self):
        return User.query.join(Donor).filter(Donor.donor_id == self.creator_id).first()

    def get_num_donors(self):
        return Donation.query.filter_by(scholarship_id=self.scholarship_id).count()

    def get_donors(self):
        query = ''' SELECT * FROM (users JOIN donors on users.id = donors.user_id) 
                    JOIN donations ON donors.donor_id = donations.donor_id 
                    WHERE donations.scholarship_id = {}
                '''
        return db.session.execute(query.format(self.scholarship_id))
        # return db.session.query(User).join(Donor).join(Donation).filter(Donation.scholarship_id == self.scholarship_id).distinct().all()

    def __repr__(self):
        return '<Scholarship %r>' % (self.name)


class Donation(db.Model):
    __tablename__ = 'donations'
    donation_id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('donors.donor_id'))
    scholarship_id = db.Column(db.Integer, db.ForeignKey('scholarships.scholarship_id'))
    amount = db.Column(db.Float, nullable=False)
    message = db.Column(db.Text(500), nullable=True)
    cleared = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Donation %r>' % (self.donation_id)






