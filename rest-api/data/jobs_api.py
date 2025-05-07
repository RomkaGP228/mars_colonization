import flask
from flask import jsonify
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint('jobs_api',
                            __name__,
                            template_folder="templates")


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict() for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_jobs(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Работа не найдена!'})
    return jsonify(
        {
            'job': jobs.to_dict()
        }
    )
