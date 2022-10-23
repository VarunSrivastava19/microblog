from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Objective: Load some shitty website built using React.js!'
