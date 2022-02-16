from flask import Blueprint, render_template

# menu blueprint definition

pictures = Blueprint('pictures', __name__, static_folder='static', static_url_path='/pictures', template_folder='templates')


# Routes
@pictures.route('/pictures')
def index():
    return render_template('pictures.html')
