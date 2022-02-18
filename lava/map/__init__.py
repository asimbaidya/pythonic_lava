from flask import render_template, Blueprint

map = Blueprint('map', __name__)

@map.route('/map')
def maps():
    return render_template('map.html')
