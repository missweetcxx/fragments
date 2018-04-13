import logging

import yaml
from os import path

ROOT_PATH = path.abspath(path.join(path.dirname(__file__)))
CONF_FILE = path.join(ROOT_PATH, 'common/conf.yaml')

with open(CONF_FILE, 'r') as f:
    CONFIG = yaml.load(f)


def logger_config():
    logging.basicConfig(level=logging.INFO)

    # config stream log
    console = logging.StreamHandler()
    console.setFormatter(fmt=logging.Formatter(CONFIG['FORMAT']['LOG_FORMAT']))
    logging.getLogger('').addHandler(console)
