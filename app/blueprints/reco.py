# -*- coding: utf-8 -*-
from flask import Blueprint, request
from ..utils.speech_client import transcript
from flask_json import as_json

reco_blueprint = Blueprint(name='reco', import_name=__name__, url_prefix='/api/')

@as_json
@reco_blueprint.route('transcript', methods=['POST'])
def reco():
    data = request.get_json(force=True)
    response_result = transcript(data.get('content'))
    return response_result
