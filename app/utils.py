from app import db
from app.models import Room
import string
from random import choice

def new_room_link():
	links = [l.link for l in Room.query.all()]
	allchars = string.ascii_letters + string.digits
	link = "".join(choice(allchars) for x in range(10))
	while link in links:
		link = "".join(choice(allchars) for x in range(10))
	return link