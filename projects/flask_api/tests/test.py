import pytest
from projects.flask_api.db.models import Task
from requests import get, post

from projects.flask_api.db.db import DB
from projects.flask_api.utils.rand_utils import RandUtils


@pytest.fixture(scope='session')
def db_session():
    db = DB()
    return db.session


def test_post_create_task(db_session):
    data = {
        "task": RandUtils.rand_str(prefix='test-', length=5),
        "priority": RandUtils.rand_int(length=1),
        'owner': 'cxx1'
    }
    res = post('http://localhost:5000/task/api/createTask', data=data).json()
    assert res['success'] is True

    record = db_session.query(Task).filter(Task.task == data['task']).one()
    assert record.priority == data['priority']

    params = {'task': data['task']}
    res = get('http://localhost:5000/task/api/getTask', params=params).json()
    assert res['success'] is True
    assert res['value']['priority'] == str(data['priority'])

    data = {
        'task': data['task'],
        'status': 2
    }
    res = post('http://localhost:5000/task/api/editTask', data=data).json()
    assert res['success'] is True
