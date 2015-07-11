from crowdscholar import db

from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class TBLUser(db.Model):
    __tablename__ = 'tbl_user'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(45))

