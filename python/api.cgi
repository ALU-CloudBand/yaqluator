#!/usr/local/bin/python2.7
# TODO


from wsgiref.handlers import CGIHandler
from api import app

CGIHandler().run(app)
