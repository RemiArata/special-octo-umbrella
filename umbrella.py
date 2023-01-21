from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home() -> None:
    return '<h>Hello World</h>'

@app.route('/user/<name>')
def user(name: str) -> None:
    return f'<h>Hello, {name.capitalize()}!</h>'

@app.route('/visit')
def visit():
    user = request.headers.get('User-Agent')
    return f'<h>You are visiting from: {user}</h>'

@app.route('/search')
def search():
    return redirect('http://google.com')