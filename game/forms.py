from flask_wtf import FlaskForm
from wtforms import * # TODO: Select imports
from wtforms.validators import InputRequired
from view import View

class SubmitForm(FlaskForm):
    mapsize = IntegerField('MapSize', validators=[InputRequired()])
    submit = SubmitField('Submit')

class MainMenu(FlaskForm):
    """
    zip_list takes in a list from our View class.
    First it removes the number display [n]
    Then it will zip to a tuple (num_choise, type)
    """
    def zip_list(to_zip):
        to_zip = [i[4:] for i in to_zip]
        return list(zip(range(1, len(to_zip)+1), to_zip))

    classes_zipped = zip_list(View.choose_role[1:])
    maps_zipped = zip_list(View.choose_size[1:])
    startloc_zipped = zip_list(View.start_location[1:])


    class_radio = RadioField("class_choice", choices=classes_zipped,
                                validators=[InputRequired()])
    maps_radio = RadioField("map_choice", choices=maps_zipped,
                                validators=[InputRequired()])
    startloc_radio = RadioField("startloc_choice", choices=startloc_zipped,
                                validators=[InputRequired()])
    submit = SubmitField('Submit')
