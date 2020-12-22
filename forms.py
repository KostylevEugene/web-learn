from flassk_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField         #импорт типов полей
from wtforms.validators import DateRequired         # импорт валидатора - класс проверки данных

class FlaskLogin(FlaskForm):
    username = StringField('Имя пользователя', validate)