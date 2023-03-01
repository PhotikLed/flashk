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
