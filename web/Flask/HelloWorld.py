# coding=utf-8
from flask import Flask
app = Flask(__name__)
app.debug = True
@app.route('/')
def hello_world():
    return 'Hello world!'
@app.route('/item/<string:id>/')
def item(id):
    return 'hello item {}'.format(id)
@app.route('/projects/')
def projects():
    return 'project'

if __name__ == '__main__':
    app.run('localhost',9000)
