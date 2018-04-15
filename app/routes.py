from app import app, db
from app.forms import LoginForm, RegisterForm, NewRoomForm
from app.models import User, Room
from app.utils import new_room_link
from flask import render_template, flash, request, \
									url_for, redirect, session
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
	if current_user.is_authenticated:
		return redirect(url_for('profile'))
	return render_template('index.html', title="BlueBoard")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('profile'))
	title = "BlueBoard | Log In"
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid email or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('profile')
		return redirect(next_page)
	return render_template('login.html', title=title, form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('portfolio'))
	title = "BlueBoard | New Room"
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Success! You can login to your new account.')
		return redirect('login')
	return render_template('register.html', form=form, title=title)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
	title = "Welcome " + current_user.email
	return render_template('profile.html', title=title, rooms=current_user.rooms)

@app.route('/profile')

@app.route('/room/<link>')
@login_required
def room(link):
	r = current_user.rooms.filter_by(link=link).first()
	if r is None:
		flash('You cannot join a room without an invite!')
		return redirect(url_for(home))
	title = "BlueBoard | " + link
	session['room'] = link
	session['email'] = current_user.email
	return render_template('room.html', title=title, room=r)

@app.route('/profile/new-room', methods=['GET', 'POST'])
@login_required
def new_room():
	form = NewRoomForm()
	if form.validate_on_submit():
		link = new_room_link()
		room = Room(link=link, nickname=form.nickname.data)
		current_user.rooms.append(room)
		db.session.commit()
		return redirect(url_for('profile'))
	title = "BlueBoard | New Room"
	return render_template('new-room.html', title=title, form=form)