from app import db
from app import constants

# base models for other tables to inherit
class Base(db.Model):
    __abstract__ = True
    user_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    role = db.Column(db.SmallInteger, default=constants.USER)
    status = db.Column(db.SmallInteger, default=constants.NEW)

    def __init__(self, first_name, last_name, email, password):
        self.first_name  = first_name
        self.last_name  = last_name
        self.email = email
        self.password = password

    def getStatus(self):
      return constants.STATUS[self.status]

    def getRole(self):
      return constants.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)

# Define a Student model
class Student(Base):
    __tablename__ = 'students'


# Define a Student model
class Donor(Base):
    __tablename__ = 'donors'
