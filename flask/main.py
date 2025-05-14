from flask import Flask, url_for
from os.path import join

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def wrds():
    return 'И на Марсе будут яблони цвести!'


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
</head>
<body>
<h1>Жди нас, Марс!</h1>
<div class="image_mars">
    <img src="{url_for('static', filename='img/image_mars.png')}"
         alt="здесь должна была быть картинка, но не нашлась">
    <p>Вот она какая, красная планета</p>
</div>
</body>
</html>'''


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <title>Колонизация</title>
    </head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <div>
        <img src="{url_for('static', filename='img/image_mars.png')}"
             alt="здесь должна была быть картинка, но не нашлась">
    </div>
    <div class="alert alert-dark">Человечество вырастает из детства.</div>
        <div class="alert alert-success">Человечество вырастает из детства.</div>
        <div class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пол планеты.</div>
        <div class="alert alert-warning">И начнем с Марса!</div>
        <div class="alert alert-danger">Присоединяйся!</div>
    </body>
    </html>'''


@app.route('/astronaut_selection')
def astronaut_selection():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Отбор астронавтов</title>
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
          crossorigin="anonymous"
        />
        <link rel="stylesheet" href="%%%PATH%%%" />
      </head>
      <body>
        <div class="d-flex flex-column align-items-center">
          <h1>Анкета претендента</h1>
          <h2>на участие в миссии</h2>
          <form class="p-3 rounded form border border-secondary">
            <div class="mb-3">
              <input
                type="text"
                class="form-control mb-1"
                placeholder="Введите фамилию"
              />
              <input
                type="text"
                class="form-control mb-2"
                placeholder="Введите имя"
              />
              <input
                type="email"
                class="form-control"
                placeholder="Введите адрес почты"
              />
            </div>
            <div class="mb-3">
              <label for="education">Какое у Вас образование?</label>
              <select name="" id="education" class="form-select">
                <option value="initial">Начальное</option>
                <option value="average">Среднее</option>
                <option value="higher">Высшее</option>
              </select>
            </div>
            <div class="mb-3">
              <p>Ваша профессия/профессии</p>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession1" />
                <label for="profession1">Инженер-исследователь</label>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession2" />
                <label for="profession2">Инженер-строитель</label>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession3" />
                <label for="profession3">Пилот</label>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession4" />
                <label for="profession4">Метеоролог</label>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession5" />
                <label for="profession5">Инженер по жизнеобеспечению</label>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession6" />
                <label for="profession6">Инженер по радиационной защите</label>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession7" />
                <label for="profession7">Врач</label>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="profession8" />
                <label for="profession8">Экзобиолог</label>
              </div>
            </div>
            <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
            <div class="mb-3">
              <label for="essay">Почему Вы хотите принять участие в миссии?</label>
              <textarea name="" id="essay" rows="5" class="form-control"></textarea>
            </div>
            <div class="mb-3">
              <label for="photo">Приложите фотографию</label>
              <input type="file" class="form-control" id="photo" />
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="ready-to-live" />
              <label for="ready-to-live" class="form-check-label"
                >Готовы остаться на Марсе?</label
              >
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
          </form>
        </div>

        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
          crossorigin="anonymous"
        ></script>
      </body>
    </html>

    """




@app.route('/results/<nick>/<int:level>/<float:rating>')
def results(nick: str, level: int, rating: int):
    str_level = str(level)
    str_rating = str(rating)
    code = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Колонизация Марса</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <div class="p-5">
      <h1>Результат отбора</h1>
      <h2>Претендент на участие в миссии %NICK%:</h2>
      <div class="alert alert-success">Поздравляем!</div>
      <ul class="list-group mb-3">
        <li class="list-group-item"><b>Ваш уровень: %LEVEL%</b></li>
        <li class="list-group-item">Ваш рейтинг: %RAITING%</li>
      </ul>
      <div class="alert alert-warning">Желаем удачи!</div>
    </div>
  </body>
  <script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
    crossorigin="anonymous"
  ></script>
</html>"""
    return code.replace('%NICK%', nick).replace('%LEVEL%', str_level).replace('%RAITING%', str_rating)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
