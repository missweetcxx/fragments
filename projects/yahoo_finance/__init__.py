#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging


def config_logger():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


config_logger()
