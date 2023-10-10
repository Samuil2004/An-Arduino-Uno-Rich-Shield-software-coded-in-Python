from flask import Flask
from flask import render_template
from flask import request, redirect
import random
import time
import datetime


app = Flask(__name__)

sample_list = []
max_samples = 15

def current_time():
    current_time = datetime.datetime.now()
    ftime = current_time.strftime("%m/%d/%Y, %H:%M:%S")
    return ftime

def light_level_measurement():
    return round(random.uniform(0,1000),2)


@app.route('/')
def index():
    global sample_list
    time_now = current_time()
    light_level = light_level_measurement()
    sample_list.append((time_now,light_level))
    sample_list = sample_list[-max_samples:]
    return render_template('subpointA.html', sample = sample_list)

if __name__ == '__main__':
    app.run(debug= True)









# app = Flask(__name__)


# @app.route('/')
# def volunteer_page():
#     return render_template('index.html',
#                             volunteers = volunteeringTestData)
