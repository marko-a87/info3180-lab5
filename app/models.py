# Add any model classes for Flask-SQLAlchemy here

from . import db

from datetime import datetime
class Movie(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    description=db.Column(db.Text)
    poster = db.Column(db.String(40))
    created_at = db.Column(db.DateTime, default=datetime.now())    

#Create a Movie model that stores the date that the movie is created at



    def __repr__(self):
        return '<Movie %r>' % self.title
