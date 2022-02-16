from flask import Blueprint, render_template

# checkout blueprint definition
from utilities.db import Cart_Query

checkout = Blueprint('checkout', __name__, static_folder='static', static_url_path='/checkout', template_folder='templates')


# Routes
@checkout.route('/checkout/<orderID>',  methods = ['GET', 'POST'])
def index(orderID):
    q = Cart_Query.Cart_Query()
    productsInOrder = q.getProductsInOrder(orderID)
    total_price = q.getTotalOrderPrice(orderID)
    return render_template('checkout.html', productsInOrder=productsInOrder, total_price=total_price)


