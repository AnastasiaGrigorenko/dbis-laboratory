from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class SymptomForm(FlaskForm):

    symptom_id = StringField('id', validators=[DataRequired(), Length(8)])

    description = StringField('description', validators=[DataRequired(), Length(50)])

    submit = SubmitField("Save")

