# 1
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


# 4
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


# 5
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


# 6

import pytest
import requests
from data.db_session import create_session, global_init
from data.jobs import Jobs

base_url = 'http://127.0.0.1:5000'


@pytest.fixture
def db_init():
    global_init("db/mars_explorer.db")


def test_post_job(db_init):
    data = {'team_leader': 1, 'job': 'описание', 'work_size': 3}
    response = requests.post(base_url + '/api/jobs', json=data)
    assert response.json() == {'success': 'OK'}


def test_post_empty(db_init):
    response = requests.post(base_url + '/api/jobs', json={})
    assert response.json() == {'error': 'Empty request'}


def test_post_bad_job(db_init):
    data = {'team_leader': 1, 'job': 'описание'}
    response = requests.post(base_url + '/api/jobs', json=data)
    assert response.json() == {'error': 'Bad request'}


def test_post_job_double(db_init):
    data = {'id': 1, 'team_leader': 1, 'job': 'описание', 'work_size': 3}
    response = requests.post(base_url + '/api/jobs', json=data)
    assert response.json() == {'error': 'Id already exists'}
