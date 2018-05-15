#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TaskStatus:
    ONGOING = 1
    COMPLETED = 2

    _VALUE_TO_NAME = {
        1: 'ONGOING',
        2: 'COMPLETED'
    }

    @staticmethod
    def get_status_by_value(value):
        return TaskStatus._VALUE_TO_NAME.get(value)

    @staticmethod
    def get_status():
        return TaskStatus._VALUE_TO_NAME.keys()
