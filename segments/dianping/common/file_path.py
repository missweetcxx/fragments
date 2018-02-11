#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path

from segments.dianping.config import CONFIG, ROOT_PATH


class FilePath:
    AVG_PRICE_BY_CITY_POP = path.join(ROOT_PATH, CONFIG['FILE']['AVG_PRICE_BY_CITY_POP'])
