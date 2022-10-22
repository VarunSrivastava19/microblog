from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Next Objective: Load some shitty website kek!'
