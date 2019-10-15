from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired

class SubmitForm(FlaskForm):
    mapsize = IntegerField('MapSize', validators=[InputRequired()])
    submit = SubmitField('Submit')
