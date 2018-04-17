from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

rooms = db.Table(
	'rooms',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('room_id', db.Integer, db.ForeignKey('room.id'), primary_key=True)
)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True)
	password_hash = db.Column(db.String(128))
	rooms = db.relationship('Room', secondary=rooms, 
												  backref=db.backref('users', lazy='dynamic'), lazy='dynamic')

	def __repr__(self):
		return '<User %s>' % self.email

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Room(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String(10), unique=True)
	nickname = db.Column(db.String(32))

	def __repr__(self):
		return '<Room %s' % self.link

@login.user_loader
def load_user(id):
	return User.query.get(int(id))