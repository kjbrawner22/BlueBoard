from flask import session
from flask_socketio import emit, join_room, leave_room
from app import socketio

@socketio.on('connected')
def connected(msg):
	room = session.get('room')
	email = session.get('email')
	join_room(room)
	email = email.split('@')
	emit('status', {'msg': 'User ' + email[0] + ' has joined the room'}, room=room)

@socketio.on('disconnected')
def disconnected():
	pass

@socketio.on('text change')
def text_change(data):
	room = session.get('room')
	emit('updated text', data, broadcast=True, include_self=False, room=room)

@socketio.on('send message')
def send_message(data):
	room = session.get('room')
	email = session.get('email')
	msg = "{" + email + "}: " + data['msg']
	emit('receive message', {'msg': msg}, broadcast=True, room=room)