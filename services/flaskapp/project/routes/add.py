from flask import Blueprint, render_template, redirect, request, url_for
from project.models import thing
from ..forms import ThingForm
from ..extensions import db

add = Blueprint('add', __name__, template_folder='templates')


@add.route('/add', methods=['GET', 'POST'])
def add_thing():
    form = ThingForm(request.form)
    if request.method == 'POST':
        t = thing.Thing(form['name'].data, form['description'].data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('add.html', form=form)
