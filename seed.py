#!/usr/bin/env python3

from server.app import app
from server.models import db
# we'll import model classes later once they exist

with app.app_context():
    # reset data and add new example data, committing to db
    pass