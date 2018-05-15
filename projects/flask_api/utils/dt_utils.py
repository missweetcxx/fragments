#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time


class DatetimeUtils(object):
    ONE_DAY_MS = 60 * 60 * 24 * 1000
    ONE_HOUR_MS = 60 * 60 * 1000

    @staticmethod
    def datetime_delta(days=0, seconds=0, microseconds=0, minutes=0, hours=0, weeks=0, format="%Y-%m-%d"):
        d = datetime.date.today() + datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds,
                                                       minutes=minutes, hours=hours, weeks=weeks)
        return d.strftime(format)

    @staticmethod
    def timestamp_delta(days=0, seconds=0, microseconds=0, minutes=0, hours=0, weeks=0):
        now = datetime.datetime.now()
        date_timestamp = time.mktime((now + datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds,
                                                               minutes=minutes, hours=hours, weeks=weeks)).timetuple()) * 1000
        return int(date_timestamp)

    @staticmethod
    def timestamp(datetime, format="%Y-%m-%d"):
        '''
        :param datetime: '2017-04-01'
        :param format: '%Y-%m-%d'
        :return: 1490976000000
        '''
        time_array = time.strptime(str(datetime), format)
        time_stamp = int(time.mktime(time_array))

        return time_stamp * 1000

    @staticmethod
    def datetime(timestamp, format="%Y-%m-%d"):
        '''
        :param timestamp: 1490976000000
        :param format: '%Y-%m-%d'
        :return: '2017-04-01'
        '''
        other_format_time = time.strftime(format, time.localtime(timestamp / 1000.0))
        return other_format_time
