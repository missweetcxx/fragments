#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from projects.dianping.common.file_path import FilePath


class ClearFile:
    @staticmethod
    def clear_avg_price_records():
        if os.path.isfile(FilePath.AVG_PRICE_BY_CITY_POP):
            os.remove(FilePath.AVG_PRICE_BY_CITY_POP)

    @staticmethod
    def clear_ex_avg_price_records():
        if os.path.isfile(FilePath.EX_AVG_PRICE_BY_CITY):
            os.remove(FilePath.EX_AVG_PRICE_BY_CITY)
