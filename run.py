# -*- coding: utf-8 -*-
"""
POC speech recognition google API
"""

__version__ = '3.0.0'
__author__ = 'Vitor Nascimento de Araujo'

if __name__ == '__main__':
    from flex_credentials import explicit_compute_engine
    explicit_compute_engine()
    from main import app
    app.run(host='127.0.0.1', port=8080, debug=True)
