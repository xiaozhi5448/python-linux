from flask import Flask 


app = Flask(__name__)
app.debug=True

@app.route('/')
@app.route('/index/')
def index():
    return 'Index Page'

@app.route('/hello/')
def hello():
    return 'hello world'

@app.route('/user/<username>/')
def echo_user(username):
    return 'User is {}'.format(username)

@app.route('/score/<int:score>/')
def score(score):
    return 'Score is:{}'.format(score)
app.run()