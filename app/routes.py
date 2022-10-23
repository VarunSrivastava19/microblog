from flask import render_template
from app import app


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
