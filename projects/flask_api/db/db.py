#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from projects.flask_api.config import CONFIG


class DB(object):
    def __init__(self):
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(CONFIG['DB_STAGING']['USERNAME'],
                                                                                    CONFIG['DB_STAGING']['PASSWORD'],
                                                                                    CONFIG['DB_STAGING']['HOST'],
                                                                                    CONFIG['DB_STAGING']['PORT'],
                                                                                    CONFIG['DB_STAGING']['DATABASE']), echo=False)
        Session = sessionmaker()
        Session.configure(bind=engine)

        self.session = Session(autocommit=True)