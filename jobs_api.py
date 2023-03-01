import sqlite3

import flask
from flask import jsonify, make_response, request

from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'team_leader_relation.email',
                                    'job', 'work_size'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'job':
                job.to_dict(only=('id', 'team_leader_relation.id',
                                  'job', 'work_size', 'collaborators',
                                  'start_date', 'end_date',
                                  'is_finished', 'team_leader_relation.name',
                                  'team_leader_relation.surname',
                                  'team_leader_relation.email'))
        }
    )


@blueprint.route('/api/jobs', methods=["POST"])
def add_job():
    data = request.json
    if not data:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if request.json.get('id'):
        job = db_sess.query(Jobs).get(request.json.get('id'))
        if job:
            return jsonify({'error': 'Id already exists'})
    job = Jobs(**data)
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
