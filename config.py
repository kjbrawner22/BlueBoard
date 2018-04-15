import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = b'\xedo\xc7\xd8\xcc\xb0l\xe4S>\xdcn\x91"\x9a0^$\xa6\xc8\xe7{\x84>'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False