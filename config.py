import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x002.#N\xf8\xba\xf4~\xaa;\xd4SV\xf5\xf2'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    