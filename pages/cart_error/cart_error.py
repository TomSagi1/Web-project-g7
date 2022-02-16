from flask import Blueprint, render_template



cart_error = Blueprint('cart_error', __name__, static_folder='static', static_url_path='/cart_error', template_folder='templates')


# Routes
@cart_error.route('/cart_error')
def index():
    return render_template('cart_error.html')
