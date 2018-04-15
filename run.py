#!venv/bin/python3

from app import socketio, app
socketio.run(app, debug=True)