from flask import Blueprint, render_template, redirect, request, url_for
from project.models.thing import Thing
from ..forms import ThingForm
from ..extensions import db

edit = Blueprint('edit', __name__, template_folder='templates')


@edit.route('/edit/<string:id>', methods=['GET', 'POST'], endpoint='edit')
def edit_thing(id):
    thing = Thing.query.get(id)
    form = ThingForm(obj=thing)
    if request.method == 'POST':
        form.populate_obj(thing)
        db.session.add(thing)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('edit.html', thing=thing, id=id, form=form)
