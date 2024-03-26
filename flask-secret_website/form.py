from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Length(min=8, message="Metin 8 karalterden büyük olmalıdır.")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, max=16, message="Metin 8 karalterden büyük olmalıdır.")])
    submit = SubmitField(label="Log In")
