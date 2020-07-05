from mysite import app

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Приветствую тебя</h1>'