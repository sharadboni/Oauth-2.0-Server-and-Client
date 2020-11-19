from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to the Authorization Server!'


@app.route('/authorize')
def authorize():
    pass


@app.route('/token')
def token():
    pass


@app.route('/refresh')
def token_refresh():
    pass
