from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class AstronautSelectionForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    education = StringField('Образование', validators=[DataRequired()])
    main_profession = SelectField('Основная профессия', choices=[
        ('engineer-researcher', 'Инженер-исследователь'),
        ('pilot', 'Пилот'),
        ('constructor', 'Строитель'),
        ('exobiologist', 'Экзобиолог'),
        ('doctor', 'Врач'),
        ('terraformer-engineer', 'Инженер по терраформированию'),
        ('climatologist', 'Климатолог'),
        ('radiation-protection-specialist', 'Специалист по радиационной защите'),
        ('astrogeologist', 'Астрогеолог'),
        ('glaciologist', 'Гляциолог'),
        ('life-support-engineer', 'Инженер жизнеобеспечения'),
        ('meteorologist', 'Метеоролог'),
        ('rover-operator', 'Оператор марсохода'),
        ('cyber-engineer', 'Киберинженер'),
        ('navigator', 'Штурман'),
        ('drone-pilot', 'Пилот дронов')
    ], validators=[DataRequired()])
    gender = StringField('Пол', validators=[DataRequired()])
    motivation = TextAreaField('Мотивация', validators=[DataRequired()])
    stay_on_mars = BooleanField('Готовы ли остаться на Марсе?')
    photo = FileField('Фото', validators=[FileRequired()])
    submit = SubmitField('Отправить')