from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.db import Customer_Query

# menu blueprint definition

login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# Routes
@login.route('/login')
def index():
    return render_template('login.html')


@login.route('/login_user', methods=['GET', 'POST'])
def check_if_exist():
    q = Customer_Query.Customer_Query()
    error = ""
    session['login'] = False
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        users = q.get_customers()
        for u in users:
            if request.form['email'] == u.email:
                if request.form['psw'] == u.password:
                    session['login'] = True
                    session['name'] = u.first_name
                    session['last_name'] = u.last_name
                    session['email'] = u.email
                    session['userID'] = u.customerID
                    return render_template('homepage.html')
                else:
                    error = 'Password is wrong'
                    return render_template('login.html', error=error)

    error = 'Email does not exist in database'
    return render_template('login.html', error=error)


@login.route('/logout_user', methods=['GET', 'POST'])
def logout():
    session['login'] = False
    session['userID'] = ''
    session['name'] = ''
    session['last_name'] = ''
    session['email'] = ''
    return render_template('homepage.html')
