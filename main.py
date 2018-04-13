# -*- coding: utf-8 -*-
"""
POC speech recognition google API
"""

from flask import Flask
from flask_json import FlaskJSON

from app.blueprints.reco import reco_blueprint

__version__ = '3.0.0'
__author__ = 'Vitor Nascimento de Araujo'

app = Flask(__name__)
FlaskJSON(app)
app.register_blueprint(reco_blueprint)
app.url_map.strict_slashes = False
