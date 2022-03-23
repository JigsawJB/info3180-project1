"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app , db
from flask import render_template, request, redirect, url_for, flash
from app.forms import PropertyForm
from app.models import NewProperty
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jaun-Luc Brown")

@app.route('/properties/create' , methods = ['POST' , 'GET'])
def create():
    """Render the websites create page"""
    
    pform = PropertyForm()
    if request.method == 'POST' and pform.validate_on_submit():
        property_title= pform.property_title.data
        description=pform.description.data
        rooms=pform.rooms.data
        bathrooms=pform.bathrooms.data
        price=pform.price.data
        property_type =pform.property_type.data
        location =pform.location.data
        #photo=pform.photo.data
        
        photo= request.files['photo']
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        propt = NewProperty(request.form['property_title'], request.form['description'], request.form['rooms'], request.form['bathrooms'], request.form['price'], request.form['property_type'], request.form['location'], filename)
        db.session.add(propt)
        db.session.commit()

        flash('Property successfully added', 'success') 
        return redirect(url_for('properties'))

    return render_template('create.html' , form=pform)


@app.route('/properties')
def properties():
    """Render properties page"""
    prop = NewProperty.query.all()
    return render_template('properties.html', prop = prop)

@app.route('/properties/<propertyid>')
def propertyid(propertyid):
    """Render individual property page"""
    x = NewProperty.query.get(propertyid)
    return render_template('prop_id.html' , property=x)

@app.route('/uploads/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
