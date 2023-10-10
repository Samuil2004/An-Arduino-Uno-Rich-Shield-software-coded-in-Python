from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)


@app.route('/')
def init():
    return render_template('initial1.html')


@app.route('/registers', methods = ['POST'])
def receive_user():
    global user

    name = request.form['username']
    age = int(request.form['userage'])

    user = (name, age)
    print("Data received:", user)  # See console...
    return redirect('/hello1')


@app.route('/hello1')
def hello_user():
    (currentName, currentAge) = user
    return render_template('hello1.html',
                            name = currentName,
                            age = currentAge)
