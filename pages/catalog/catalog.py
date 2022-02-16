from flask import Blueprint, render_template

# menu blueprint definition
from utilities.db import Cart_Query

catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')


# Routes
@catalog.route('/catalog')
def index():
    q = Cart_Query.Cart_Query()
    products = q.getProducts()
    return render_template('catalog.html', products=products)
