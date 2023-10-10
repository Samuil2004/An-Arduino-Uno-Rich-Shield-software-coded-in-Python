from flask import Flask
from flask import render_template
from flask import request, redirect
import random
import time
import datetime

app = Flask(__name__)

# sample_list = []
# slen = 5
# def time_printer():
#     time = datetime.datetime.now()
#     current_time = time.strftime("%m/%d/%Y, %H:%M:%S")
#     return current_time

# def temperature_printer():
#     temperature = random.randint(0,100)
#     return temperature

# def listt():

# @app.route("/")
# def index():
#     global sample_list
#     time_now = time_printer()
#     temp = temperature_printer()
#     sample_list.append((time_now,temp))
#     sample_list = sample_list[-slen:]
#     return render_template('week6.html', sample = sample_list)



sample_list = [
     ("14:00", "75"),
     ("15:00", "45"),
     ("16:00", "50"),
     ("17:00", "90"),
     ("18:00", "38")
]



@app.route("/")
def index():
    global sample_list
    return render_template('week6.html', sample = sample_list)



if __name__ == '__main__':
    app.run(debug= True)
