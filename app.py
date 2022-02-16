from flask import Flask

# App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key = '123'


# Pages
# Homepage
from pages.homepage.homepage import homepage

app.register_blueprint(homepage)

# ClientsTell
from pages.clientsTell.clientsTell import clientsTell

app.register_blueprint(clientsTell)

# Contact
from pages.contact.contact import contact

app.register_blueprint(contact)

# Login
from pages.login.login import login

app.register_blueprint(login)

# Pictures
from pages.pictures.pictures import pictures

app.register_blueprint(pictures)

# Register
from pages.register.register import register

app.register_blueprint(register)

# Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers

app.register_blueprint(page_error_handlers)

# Cart
from pages.cart.cart import cart

app.register_blueprint(cart)

# Checkout
from pages.checkout.checkout import checkout

app.register_blueprint(checkout)

# Cart error
from pages.cart_error.cart_error import cart_error

app.register_blueprint(cart_error)

# Catalog
from pages.catalog.catalog import catalog

app.register_blueprint(catalog)


# Components
# Header
from components.header.header import header

app.register_blueprint(header)

# Footer
from components.footer.footer import footer

app.register_blueprint(footer)
