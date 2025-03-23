from flask import Flask, render_template, url_for

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


params = {'head1': 'Миссия Колонизация Марса', 'head4': 'И на Марсе будут яблони цвести!'}


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title, **params)


@app.route("/training/<prof>")
def training(prof):
    return render_template("prof.html", **params, prof=prof)


@app.route("/list_prof/<list>")
def list_prof(list):
    lst = ['инженер-исследователь', "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
           "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
           "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    return render_template("list_prof.html", **params, list=list, lst=lst)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    props = {"title": "Анкета", "surname": "Watny", "name": "Mark", "education": "выше среднего",
             "profession": "штурман марсохода", "sex": "male", "motivation": "Всегда мечтал застрять на Марсе!",
             "ready": "True", "style_url": url_for('static', filename="css/style.css")}
    return render_template("auto_answer.html", **props, **params)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/list_prof/ol')
    app.run(port=8080, host='127.0.0.1')
