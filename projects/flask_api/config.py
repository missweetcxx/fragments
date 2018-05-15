#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from pathlib import Path, PurePath

import yaml

ROOT_PATH = Path(__file__).resolve().parent

CONFIG = {}
for file_path in Path(ROOT_PATH).glob(r'conf/*.yaml'):
    with file_path.open() as config_file:
        CONFIG = yaml.load(config_file)


def logger_config():
    logging.basicConfig(level=logging.INFO)

    # config stream log
    console = logging.StreamHandler()
    console.setFormatter(fmt=logging.Formatter(CONFIG['LOG']['LOG_FORMAT']))
    logging.getLogger('').addHandler(console)

    # config file log
    file = logging.FileHandler(filename=PurePath(ROOT_PATH, CONFIG['LOG']['LOG_NAME']), mode='w', encoding='utf-8')
    file.setFormatter(fmt=logging.Formatter(CONFIG['LOG']['LOG_FORMAT']))
    logging.getLogger('').addHandler(file)
