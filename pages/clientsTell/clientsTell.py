from flask import Blueprint, render_template

# menu blueprint definition

clientsTell = Blueprint('clientsTell', __name__, static_folder='static', static_url_path='/clientsTell', template_folder='templates')


# Routes
@clientsTell.route('/clientsTell')
def index():
    return render_template('clientsTell.html')
