#!/usr/local/bin/python2.7


from wsgiref.handlers import CGIHandler
from api import app

CGIHandler().run(app)

