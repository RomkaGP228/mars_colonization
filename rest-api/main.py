from flask import Flask, make_response, jsonify
from data import db_session
from data import jobs_api

app = Flask(__name__)

app.config['SECRET_KEY'] = 'meee'


@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


def main():
    db_session.global_init("db/database.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
