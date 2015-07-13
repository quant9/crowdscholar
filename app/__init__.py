# Import flask and template operators
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Define the database object imported by modules and views
db = SQLAlchemy(app)
# db.create_all()

from .views.home import home
from .views.student import student_profile
from .views.donor import donor_profile

# app.register_blueprint(site, subdomain='<site_subdomain>')
# http://stackoverflow.com/questions/7512698/flask-subdomain-routing
app.register_blueprint(home)
app.register_blueprint(student_profile)
app.register_blueprint(donor_profile)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
