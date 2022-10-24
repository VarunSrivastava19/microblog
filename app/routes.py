from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
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
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
