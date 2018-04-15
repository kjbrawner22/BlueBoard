from flask import session
from flask_socketio import emit, join_room, leave_room
from app import socketio

@socketio.on('connected')
def connected():
	room = session.get('room')
	join_room(room)
	emit('status', {'msg': session.get('email') + ' just joined the room'}, room=room)