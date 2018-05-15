#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Resource, reqparse, Api

from projects.flask_api.db.assemblers import assemble_task
from projects.flask_api.db.db import DB
from projects.flask_api.db.models import Task, RegisterUser
from projects.flask_api.helper.task.constants import TaskStatus
from projects.flask_api.helper.task.wrapper import Wrapper
from projects.flask_api.utils.error_utils import Error

task = Blueprint('task', __name__, url_prefix='/task')
api_task = Api(task)


class TaskApi(Resource):
    db = DB()

    def __init__(self):
        self.db_session = TaskApi.db.session
        self.args = TaskApi.req_parse()
        self.users = self.users()
        super(TaskApi, self).__init__()

    @staticmethod
    def req_parse():
        req = reqparse.RequestParser()
        req.add_argument('task')
        req.add_argument('priority')
        req.add_argument('owner')
        req.add_argument('status')
        args = req.parse_args()

        return args

    def users(self):
        users = self.db_session.query(RegisterUser).filter(RegisterUser.forbidden==0).all()
        return [x.username for x in users]


class GetTask(TaskApi):
    def __init__(self):
        super(GetTask, self).__init__()
        self.error = self._validator()

    def _validator(self):
        if not self.args.get('task'):
            return Error.LACK_OF_PARAM
        else:
            return Error.SUCCESS

    def get(self):
        if self.error is Error.SUCCESS:
            try:
                record = self.db_session.query(Task).filter(Task.task == self.args.get('task')).all()
                priority = '' if len(record) == 0 else record[0].priority
                task = '' if len(record) == 0 else record[0].task
                owner = '' if len(record) == 0 else record[0].owner
                status = '' if len(record) == 0 else record[0].status
                return Wrapper.wrapper(self.error, priority, task, owner, status)
            except KeyError or AttributeError:
                return Wrapper.wrapper(error=Error.INTERNAL_ERROR)
            finally:
                self.db_session.close()
        else:
            return Wrapper.wrapper(self.error)


class CreateTask(TaskApi):
    def __init__(self):
        super(CreateTask, self).__init__()
        self.error = self._validator()

    def _validator(self):
        if not (self.args.get('task') and self.args.get('priority') and self.args.get('owner')):
            return Error.LACK_OF_PARAM
        elif len(self.db_session.query(Task).filter(Task.task == self.args.get('task')).all()) > 0:
            return Error.TASK_EXIST
        elif self.args.get('owner') not in self.users:
            return Error.AUTH_FAIL
        else:
            return Error.SUCCESS

    def post(self):
        if self.error is Error.SUCCESS:
            try:
                record = assemble_task(task_name=self.args.get('task'), priority=self.args.get('priority'),
                                       owner=self.args.get('owner'), status=TaskStatus.ONGOING)
                self.db_session.add(record)
                self.db_session.flush()
                return Wrapper.wrapper(self.error, priority=record.priority, task=record.task, owner=record.owner,
                                       status=TaskStatus.get_status_by_value(record.status))
            except KeyError or AttributeError:
                return Wrapper.wrapper(error=Error.INTERNAL_ERROR)
            finally:
                self.db_session.close()
        else:
            return Wrapper.wrapper(error=self.error)


class GetTaskList(Resource):
    def __init__(self):
        self.db_session = CreateTask.db.session
        super(GetTaskList, self).__init__()

    def get(self):
        try:
            tasks = self.db_session.query(Task).order_by(Task.priority).all()
            task_list = []
            for item in tasks:
                task = dict(task=item.task, priority=item.priority, owner=item.owner,
                            status=TaskStatus.get_status_by_value(item.status))
                task_list.append(task)
            return Wrapper.wrapper_list(Error.SUCCESS, task_list)
        except KeyError or AttributeError:
            return Wrapper.wrapper(error=Error.INTERNAL_ERROR)
        finally:
            self.db_session.close()


class EditTask(TaskApi):
    def __init__(self):
        super(EditTask, self).__init__()
        self.error = self._validator()

    def _validator(self):
        if not (self.args.get('task') and self.args.get('status')):
            return Error.LACK_OF_PARAM
        elif len(self.db_session.query(Task).filter(Task.task == self.args.get('task')).all()) == 0:
            return Error.TASK_NOT_EXIST
        elif int(self.args.get('status')) not in TaskStatus.get_status():
            return Error.INVALID_PARAM
        else:
            return Error.SUCCESS

    def post(self):
        if self.error == Error.SUCCESS:
            try:
                self.db_session.query(Task).filter(Task.task == self.args.get('task')).update(
                    {Task.status: self.args.get('status')}, synchronize_session=False)
                self.db_session.flush()
                item = self.db_session.query(Task).filter(Task.task == self.args.get('task')).one()
                self.db_session.refresh(item)
                return Wrapper.wrapper(error=Error.SUCCESS, task=item.task, priority=item.priority, owner=item.owner,
                                       status=TaskStatus.get_status_by_value(item.status))
            except Exception:
                return Wrapper.wrapper(error=Error.INTERNAL_ERROR)
            finally:
                self.db_session.close()
        else:
            return Wrapper.wrapper(error=self.error)


api_task.add_resource(CreateTask, '/api/createTask')
api_task.add_resource(GetTask, '/api/getTask')
api_task.add_resource(GetTaskList, '/api/getTaskList')
api_task.add_resource(EditTask, '/api/editTask')
