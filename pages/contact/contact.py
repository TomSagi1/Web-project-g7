from flask import Blueprint, render_template, request
from utilities.db import Contact_Query

# menu blueprint definition

contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')


# Routes
@contact.route('/contact')
def index():
    return render_template('Contact.html')

@contact.route('/contact_us' , methods=['GET', 'POST'])
def insert_contact():
    q = Contact_Query.Contact_Query()
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        message = request.form['comment']
        q.insert_message(first_name, last_name, email, message)
        success = 'Message received!'
        return render_template('contact.html', success=success)
    return render_template('contact.html')
