from flask import Blueprint, render_template
from ..extensions import db
from ..models.thing import Thing

poem = Blueprint('poem', __name__)


@poem.route('/poem')
def poem_text():
    return render_template('poem.html')
