"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file,flash
from app.forms import  MovieForm
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from app.models import Movie
import os
from flask import send_from_directory


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@app.route("/api/v1/movies", methods=['POST'])
def movies():
    movieForm = MovieForm()
    if movieForm.validate_on_submit():
        form_title = movieForm.title.data
        form_description = movieForm.description.data
        form_poster = movieForm.poster.data

        movie = Movie(title =form_title, description =form_description, poster=form_poster.filename)
        db.session.add(movie)
        secure_image = secure_filename(form_poster.filename)
        form_poster.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_image))
        db.session.commit()
        flash("Added movie successfully", "success")
        return {
            "message": "Movie Successfully added",
            "title": form_title,
            "poster": form_poster.filename,
            "description": form_description
        }

    else:
        form_errors_lst = form_errors(movieForm)
        lst_of_errors = []
        for error in form_errors_lst:
            error_dict = {}
            error_field, error_text = error.split('-')
            error_dict[error_field] = error_text
            lst_of_errors.append(error_dict)
        return jsonify({
            "errors":lst_of_errors
        })
       
@app.route("/api/v1/movies", methods=['GET'])
def get_movies():
    Movies = Movie.query.all()
    movies_lst= []
    
    for movie in Movies:
       data= {
           "id": movie.id,
           "title": movie.title,
           "description": movie.description,
           "poster": movie.poster
        }
    
       movies_lst.append(data)
    return {
        "movies": movies_lst
    }


@app.route("/api/v1/posters/<filename>")
def get_images(filename):
    image = send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)
    return image
       
@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    
    return jsonify({'csrf_token':generate_csrf()})

