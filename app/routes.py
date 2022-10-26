from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Lil Jack'}
    posts = [
        {
            'author': {'username': 'Roman'},
            'body': 'LC is cool man!',
        },
        {
            'author': {'username': 'Tony Prince'},
            'body': 'LS is the way to go now!',
        },
        {
            'author': {'username': 'Johny Klebitz'},
            'body': 'LC Chapter is now done, LS is next. LOST FOREVER!',
        },
        {
            'author': {'username': 'Pegerino'},
            'body': 'LC is full of flying rats!',
        },
    ]
    return render_template('index.html', title='Home Page', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page) != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Bingo! You are now registered successfully!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

