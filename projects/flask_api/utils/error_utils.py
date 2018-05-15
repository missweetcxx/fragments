#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Error:
    SUCCESS = {'desc': 'success', 'success': True, 'code': 10000}
    LACK_OF_PARAM = {'desc': 'lack of param', 'success': False, 'code': 10010}
    TASK_EXIST = {'desc': 'task has been existed', 'success': False, 'code': 10020}
    INTERNAL_ERROR = {'desc': 'internal error', 'success': False, 'code': 10030}
    INVALID_PARAM = {'desc': 'invalid param', 'success': False, 'code': 10040}
    THIRD_PARTY_ERROR = {'desc': 'third party error', 'success': False, 'code': 10050}
    TASK_NOT_EXIST = {'desc': 'task not exist', 'success': False, 'code': 10060}
    AUTH_FAIL = {'desc': 'auth fail', 'success': False, 'code': 10070}
