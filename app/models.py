from app import db
from app import constants
from flask.ext.login import UserMixin
import datetime
from sqlalchemy import func

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
    is_student = db.relationship('Student', backref='users')
    is_donor = db.relationship('Donor', backref='users')

    def get_status(self):
        return constants.STATUS[self.status]

    def get_user_type(self):
        return constants.USERTYPE[self.user_type]

    def __repr__(self):
        return '<User %r>' % (self.first_name)

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gender = db.Column(db.SmallInteger, nullable=False)
    address = db.Column(db.String(300), nullable=False)
    apt_no = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    hs_year = db.Column(db.SmallInteger(), nullable=False)
    dob = db.Column(db.DateTime(), nullable=False)

    # "Federal guidelines mandate that we collect data on the legal sex of all applicants.
    # Please report the sex currently listed on your birth certificate. 
    # If you wish to provide more details regarding your sex or gender identity, 
    # please do so in the Additional Information section."
    applications = db.relationship('Application', backref='students')

    @classmethod
    def get_student(cls, user_id=None, student_id=None):
        if user_id:
            return Donor.query.filter_by(user_id=user_id).first()
        if student_id:
            return Donor.query.filter_by(student_id=student_id).first()
        return None

    def get_user(self):
        return User.query.filter_by(id=self.user_id).first()


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
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(10), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    alma_mater = db.Column(db.String(100), nullable=True)
    profession = db.Column(db.String(100), nullable=True)
    company = db.Column(db.String(200), nullable=True)
    bio = db.Column(db.Text(1000), default="I'm proud to be a donor on Crowdscholar!")
    scholarships_created = db.relationship('Scholarship', backref='donors')
    donations = db.relationship('Donation', backref='donors')

    @classmethod
    def get_donor(cls, user_id=None, donor_id=None):
        if user_id:
            return Donor.query.filter_by(user_id=user_id).first()
        if donor_id:
            return Donor.query.filter_by(donor_id=donor_id).first()
        return None

    def get_user(self):
        return User.query.filter_by(id=self.user_id).first()

    def get_total_donated(self):
        query = ''' SELECT scholarship.name, donation.amount 
                    FROM donations JOIN scholarships ON donations.scholarship_id = scholarships.scholarship_id
                    WHERE donation.donor_id = {}
                '''
        return db.session.execute(query.format(self.donor_id))


class Scholarship(db.Model):
    __tablename__ = 'scholarships'
    scholarship_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('donors.donor_id'))
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.Text, nullable=False)
    amount_target = db.Column(db.Float, nullable=False)
    amount_funded = db.Column(db.Float, default=0)
    status = db.Column(db.Integer, default=constants.FUNDING)
    description = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    expiration_date = db.Column(db.DateTime, default=datetime.datetime(2099,12,31))
    donations_to = db.relationship('Donation', backref='scholarships')
    applications_to = db.relationship('Application', backref='scholarships')

    @classmethod
    def get_scholarship(cls, s_id):
        return Scholarship.query.join(Donor).filter(Scholarship.scholarship_id == s_id).first()

    def get_creator(self):
        return User.query.join(Donor).filter(Donor.donor_id == self.creator_id).first()

    def get_num_donors(self):
        return Donation.query.filter_by(scholarship_id=self.scholarship_id).count()

    def get_donors(self):
        query = ''' SELECT * FROM (users JOIN donors ON users.id = donors.user_id) 
                    JOIN donations ON donors.donor_id = donations.donor_id 
                    WHERE donations.scholarship_id = {}
                '''
        return db.session.execute(query.format(self.scholarship_id))

    def get_num_applications(self):
        pass

    def get_applicants(self):
        pass

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


class Application(db.Model):
    __tablename__ = 'applications'
    app_id = db.Column(db.Integer, primary_key=True)
    scholarship_id = db.Column(db.Integer, db.ForeignKey('scholarships.scholarship_id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    question_1 = db.Column(db.String(500), nullable=False)
    answer_1 = db.Column(db.Text(5000), nullable=False)
    question_2 = db.Column(db.String(500), nullable=True)
    answer_2 = db.Column(db.Text(5000), nullable=True)
    question_3 = db.Column(db.String(500), nullable=True)
    answer_3 = db.Column(db.Text(5000), nullable=True)
    question_4 = db.Column(db.String(500), nullable=True)
    answer_4 = db.Column(db.Text(5000), nullable=True)
    question_5 = db.Column(db.String(500), nullable=True)
    answer_5 = db.Column(db.Text(5000), nullable=True)
    bool_q1 = db.Column(db.String(500), nullable=True)
    bool_a1 = db.Column(db.Boolean(), nullable=True)
    select_q1 = db.Column(db.Text(500), nullable=True)
    select_a1 = db.Column(db.String(100), nullable=True)
    select_q2 = db.Column(db.Text(500), nullable=True)
    select_a2 = db.Column(db.String(100), nullable=True)
    select_q3 = db.Column(db.Text(500), nullable=True)
    select_a3 = db.Column(db.String(100), nullable=True)
    upload_q1 = db.Column(db.Text(500), nullable=True)
    upload_a1 = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<Application %r>' % (self.app_id)

