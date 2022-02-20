from flask import render_template, Blueprint

todo = Blueprint('todo', __name__)

@todo.route('/ycd')
def ycd():
    return render_template('youcando.html')

@todo.route('/clean_air')
def clean_air():
    return render_template('clean_air.html')

