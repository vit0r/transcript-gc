# -*- coding: utf-8 -*-
"""
POC speech recognition google API
"""

import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

client = speech.SpeechClient()

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='pt-BR')


def transcript(content):
    audio = types.RecognitionAudio(content=content)
    response = client.recognize(config, audio)
    return response.results
