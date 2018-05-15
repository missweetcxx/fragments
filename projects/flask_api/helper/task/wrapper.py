#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_restful import fields, marshal


class Fields:
    value_fields = {
        'task': fields.String(attribute='task'),
        'priority': fields.String(attribute='priority'),
        'owner': fields.String(attribute='owner'),
        'status': fields.String(attribute='status')
    }

    resource_fields = {
        'success': fields.Boolean,
        'desc': fields.String,
        'value': fields.Nested(value_fields)
    }

    list_fields = {
        'success': fields.Boolean,
        'desc': fields.String,
        'value': fields.List(fields.Nested(value_fields))
    }


class Wrapper:
    @staticmethod
    def _data(error, priority, task, owner, status):
        return dict(success=error['success'], desc=error['desc'], value=dict(task=task, priority=priority, owner=owner, status=status))

    @staticmethod
    def _data_list(error, task_list):
        return dict(success=error['success'], desc=error['desc'], value=task_list)

    @staticmethod
    def wrapper(error, priority='', task='', owner='', status=''):
        data = Wrapper._data(error, priority, task, owner, status)
        return marshal(data, Fields.resource_fields)

    @staticmethod
    def wrapper_list(error, value_list):
        wrapped_value = []
        for value in value_list:
            wrapped_value.append(marshal(value, Fields.value_fields))
        data = Wrapper._data_list(error, wrapped_value)
        return marshal(data, Fields.list_fields)
