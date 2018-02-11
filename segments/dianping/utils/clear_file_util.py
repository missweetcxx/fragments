#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from segments.dianping.common.file_path import FilePath


class ClearFile:
    @staticmethod
    def clear_avg_price_records():
        if os.path.isfile(FilePath.AVG_PRICE_BY_CITY_POP):
            os.remove(FilePath.AVG_PRICE_BY_CITY_POP)
