import flask
from flask import jsonify, request, make_response
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


@blueprint.route('/api/jobs/<job_id>')
def get_job_error(job_id: not int):
    return jsonify({'error': 'Bad request'}), 401


@blueprint.route('/api/jobs', methods=['POST'])
def create_news():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader_id', 'job', 'work_size', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Jobs(team_leader=request.json['team_leader_id'], job=request.json['job'], work_size=int(
        request.json['work_size']), collaborators=request.json['collaborators'],
               is_finished=request.json['is_finished'])
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})
