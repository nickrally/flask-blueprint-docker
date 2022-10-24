from flask import Blueprint, render_template, redirect, request, url_for
from project.models import thing
from ..forms import ThingForm
from ..extensions import db

delete = Blueprint('delete', __name__, template_folder='templates')


@delete.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_thing(id):
    t = thing.Thing.query.get(id)
    if request.method == 'POST':
        db.session.delete(t)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('delete.html', thing=t, id=id)
