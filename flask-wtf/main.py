from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = "goida"

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    params = {'head1': 'Миссия Колонизация Марса', 'head4': 'И на Марсе будут яблони цвести!'}
    return render_template("base.html", title=title, **params)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/')
    app.run(port=8080, host='127.0.0.1')
