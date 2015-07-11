# Import flask and template operators
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from .views.student import student_profile
from .views.donor import donor_profile

app = Flask(__name__)

# app.register_blueprint(site, subdomain='<site_subdomain>')
# http://stackoverflow.com/questions/7512698/flask-subdomain-routing
app.register_blueprint(student_profile, url_prefix='/<student_id>')
app.register_blueprint(donor_profile, url_prefix='/<donor_id>')
app.register_blueprint()

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
db.create_all()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
