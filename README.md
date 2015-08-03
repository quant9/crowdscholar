Crowdscholar
============
www.crowdscholar.org

Setup instructions
------------
 1. Clone the repo, setup virtualenv, install dependencies from requirements.txt
 2. Create a file called `instance/config.py` with the following:
        SECRET_KEY = 'crowdscholar345'
        SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/crowdscholar'
any other configuration variables specified here will override the existing `~/config.py`.
 3. Make a local mysql database 'crowdscholar'
 4. Setup databases using the following commands within python shell:
        from app import db
        db.create_all()  # creates local mysql db and tables`
 5. Launch app with `python run.py`
