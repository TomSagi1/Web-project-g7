from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.db import Customer_Query

# about blueprint definition
register = Blueprint('register', __name__, static_folder='static', static_url_path='/register', template_folder='templates')


# Routes
@register.route('/register')
def index():
    return render_template('register.html')


@register.route('/registrate_user', methods=['GET', 'POST'])
def registrate_user():
    q = Customer_Query.Customer_Query()
    if request.method == 'POST':
        users = q.get_customers()
        for u in users:
            if request.form['email'] == u.email:
                error = 'Email already exists in database. please choose another'
                return render_template('register.html', error=error)

    customerID = q.getLastUserId() + 1
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    email = request.form['email']
    psw = request.form['psw']
    q.insert_user(customerID, phone, email, first_name, last_name, psw)
    success = 'Users was created successfully!'
    return render_template('register.html', success=success)
