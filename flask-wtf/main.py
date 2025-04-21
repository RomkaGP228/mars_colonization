from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = "goida"

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astronaut_id = StringField('Id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])

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


@app.route("/answer", methods=['GET', 'POST'])
@app.route("/auto_answer")
def answer():
    props = {"title": "Анкета", "surname": "Watny", "name": "Mark", "education": "выше среднего",
             "profession": "штурман марсохода", "sex": "male", "motivation": "Всегда мечтал застрять на Марсе!",
             "ready": "True", "style_url": url_for('static', filename="css/style.css")}
    return render_template("auto_answer.html", **props, **params)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    props = {'emblem_url': url_for('static', filename='img/MARS-2-7.png')}
    if form.validate_on_submit():
        return redirect('/answer')
    return render_template("login.html", **props, **params, form=form)


@app.route("/distribution", methods=['GET', 'POST'])
def distribution():
    astronauts = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                  'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    props = {'astronauts': astronauts, "style_url": url_for('static', filename="css/style.css")}
    return render_template("distribution.html", **props, **params)


@app.route('/table/<gender>/<age>')
def table_param(gender: str, age: int):
    props = {'gender': gender, 'age': age, 'child_img_url': CHILD_IMG_URL, 'adult_img_url': ADULT_IMG_URL,
             'style_url': url_for('static', filename='css/main.css')}
    return render_template('table_param.html', **props)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
