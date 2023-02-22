from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, IntegerField, SelectField, \
    DateField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = SelectField("Ответственный", validtors=[DataRequired])
    job = StringField('Описание работы')
    work_size = IntegerField('Объем работы, ч')
    collaborators = StringField('Соучастники')
    start_date = DateField('Начало работы')
    end_date = DateField('Окончание работы')
    is_finished = BooleanField('Завершена')
    submit = SubmitField('Войти')
