from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    amount = DecimalField('Kwota', validators=[DataRequired()])
    submit = SubmitField('Zapisz')
