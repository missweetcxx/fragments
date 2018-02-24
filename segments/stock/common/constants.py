#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.stock.config import CONFIG

HEADER = {"User-Agent": CONFIG['HTTP']['USER_AGENT']}


class Stock:
    CODE = 0
    START_DATE = ''
    END_DATE = ''
