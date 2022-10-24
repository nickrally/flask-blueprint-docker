
from flask_wtf import FlaskForm
from wtforms import StringField


class ThingForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
