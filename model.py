# import heapq
# import time
from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


class User(db.Model):
    """ User information"""

    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=True)
    address = db.Column(db.Text, nullable=True)
    city = db.Column(db.String(50))    
    state = db.Column(db.String(50))
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10))
    role = db.Column(db.String(10))



class Course(db.Model):
    """ Neighborhood information"""

    __tablename__ = "courses"

    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    levels = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    affiliation = db.Column(db.Text)

   

class Session(db.Model):
    """save image urls"""
    __tablename__ = "sessions"

    session_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    day = db.Column(db.String(10))
    timeSlot = db.Column(db.String(50))
    capacity = db.Column(db.Integer)

    course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id), nullable=False)


class UserSession(db.Model):
    """save image urls"""
    __tablename__ = "userSessions"
    userSession_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey(Session.session_id), nullable=False)





def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///alaap'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///testdb'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)



if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."


