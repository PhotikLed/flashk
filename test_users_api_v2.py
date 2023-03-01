import pytest
import requests
from data.db_session import create_session, global_init
from data.users import User

base_url = 'http://127.0.0.1:5000'


@pytest.fixture
def db_init():
    global_init("db/mars_explorer.db")


def test_get_one_user(db_init):
    response = requests.get(base_url + '/api/v2/users/1')
    sess = create_session()
    users = sess.query(User).get(1)
    assert response.json() == {'user': users.to_dict(rules=('-jobs',))}


def test_get_wrong_user(db_init):
    user_id = 999
    response = requests.get(base_url + '/api/v2/users/999')
    assert response.json() == {'message': f'User {user_id} not found'}


def test_get_all_user(db_init):
    response = requests.get(base_url + '/api/v2/users')
    sess = create_session()
    users = sess.query(User).all()
    assert response.json() == {
        'users':
            [item.to_dict(only=('id', 'name', 'surname', 'email', 'jobs.id',
                                'jobs.job'))
             for item in users]
    }


def test_post_user(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность',
        'email': 'email2@mail.ru'
    }

    response = requests.post(base_url + '/api/v2/users', json=user_json)
    assert response.json() == {'success': 'OK'}


def test_post_user_empty(db_init):
    user_json = {}
    response = requests.post(base_url + '/api/v2/users', json=user_json)
    assert response.json() == {'message': {'name': 'Missing required parameter in'
                                                   ' the JSON body or the post body or the query string'}}


def test_post_user_wrong_missed_param(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность'
    }

    response = requests.post(base_url + '/api/v2/users', json=user_json)
    assert response.json() == {'message': {'email': 'Missing required parameter'
                                                    ' in the JSON body or the post body or the query string'}}


def test_post_user_wrong_param(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 'qwer',
        'speciality': 'Специальность',
        'email': 'email3@mail.ru'
    }

    response = requests.post(base_url + '/api/v2/users', json=user_json)
    assert response.json() == {'message': {'age': "invalid literal for int() with base 10: 'qwer'"}}


def test_post_user_wrong_already_exist(db_init):
    user_json = {
        'id': 1,
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность',
        'email': 'email4@mail.ru'
    }

    response = requests.post(base_url + '/api/v2/users', json=user_json)
    assert response.json() == {'error': 'Id already exists'}
