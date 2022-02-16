from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.db import Cart_Query

# cart blueprint definition

cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart', methods=['GET', 'POST'])
def index():
    q = Cart_Query.Cart_Query()
    products = q.getProducts()
    return render_template('cart.html', products=products)


@cart.route('/createOrder', methods=['GET', 'POST'])
def createOrder():
    q = Cart_Query.Cart_Query()
    checkInput = 0
    for temp in request.form:
        checkInput = checkInput + int(request.form[temp])
    if checkInput != 0:
        newOrderID = q.getLastOrderID() + 1
        if request.method == "POST":
            if session['login']:
                User = session['userID']
                q.createNewOrder(newOrderID, User)
                for temp in request.form:
                    if request.form[temp] != '0':
                        q.createNewProductInOrder(newOrderID, temp, request.form[temp])
                return redirect(url_for('checkout.index', orderID=newOrderID))
            else:
                error = 'please sign in first to make an order.'
                return render_template('cart_error.html', error=error)
    else:
        error = 'No products were selected.'
        return render_template('cart_error.html', error=error)

@cart.route('/sendOrder', methods=['GET', 'POST'])
def sendOrder():
    q = Cart_Query.Cart_Query()
    if request.method == "POST":
        orderID = request.form['orderID']
        q.approveOrder(orderID)
    return redirect('homepage')


@cart.route('/cancelOrder', methods=['GET', 'POST'])
def cancelOrder():
    q = Cart_Query.Cart_Query()
    if request.method == "POST":
        orderID = request.form['orderID']
        q.cancelOrder(orderID)
    return redirect('cart')