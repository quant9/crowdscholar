# Import flask and template operators
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Define the database object imported by modules and views
db = SQLAlchemy(app)
# db.create_all()

# handle login with flask-login
login_manager = LoginManager()
login_manager.login_view = 'views.home'
login_manager.login_message = u'You must be logged in to access Crowdscholar.'
login_manager.init_app(app)

# import views
from .views.home import home
from .views.student import student
from .views.donor import donor

# app.register_blueprint(site, subdomain='<site_subdomain>')
# http://stackoverflow.com/questions/7512698/flask-subdomain-routing
app.register_blueprint(home)
app.register_blueprint(student)
app.register_blueprint(donor)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
