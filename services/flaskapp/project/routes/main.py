from flask import Blueprint
from ..extensions import db
from ..models.thing import Thing

main = Blueprint('main', __name__)


@main.route('/thing/<name>')
def create_thing(name):
    thing = Thing(name=name)
    db.session.add(thing)
    db.session.commit()

    return "Created thing"
