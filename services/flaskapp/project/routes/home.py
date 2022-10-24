from flask import Blueprint, render_template
from project.models import thing

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET', 'POST'])
def index():
    things = thing.Thing.query.order_by(thing.Thing.id.asc())
    return render_template('home.html', things=things)
