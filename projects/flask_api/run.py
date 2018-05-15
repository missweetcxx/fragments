#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from projects.flask_api.api import app

Logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
