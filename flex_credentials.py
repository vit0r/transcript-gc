# -*- coding: utf-8 -*-
"""
POC speech recognition google API
"""

__version__ = '3.0.0'
__author__ = 'Vitor Nascimento de Araujo'


def explicit_compute_engine():
    from google.cloud import storage
    from os import path
    from os import environ
    credential_file = path.join(path.dirname(__file__), 'credentials', 'talk2me-fdc6386559a2.json')
    storage_client = storage.Client.from_service_account_json(credential_file)
    environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_file
    buckets = list(storage_client.list_buckets())
    print(buckets)
