#!/usr/bin/env python
import os
import subprocess

USE_VIRTUALENV = False
VENV_NAMES = ['fav_live']
VENV_PATHS = []

dirpath = os.path.dirname(__file__)
vpath=os.path.join(dirpath, '..', '..', 'virtualenvs')
VENV_PATHS.insert(0, vpath)

def which(pgm, path=None):
    if path is None:
        path = os.getenv('PATH')
    for p in path.split(os.path.pathsep):
        p = os.path.join(p, pgm)
        p = os.path.abspath(p)
        if os.path.exists(p) and os.access(p, os.X_OK):
            return p

VENV_PATH = None
for p in VENV_PATHS:
    for venv_name in VENV_NAMES:
        venv_path = os.path.join(p, venv_name)
        venv_path = os.path.abspath(venv_path)
        if os.path.exists(venv_path):
            VENV_PATH = venv_path
            break

if VENV_PATH is not None:
    path = os.path.join(VENV_PATH, 'bin', 'activate_this.py')
    execfile(path, dict(__file__=path))


confpath = os.path.abspath(os.path.join(dirpath, '..', 'conf',
                                        'gunicorn.conf'))
release_token_path = os.path.join(dirpath, '..',
                                  'jobs', 'release_tokens.py')
release_token_path = os.path.abspath(release_token_path)
subprocess.call([which('python'), release_token_path])
os.execl(which('gunicorn_django'),
         '--settings=settings',
         '-c', confpath)
