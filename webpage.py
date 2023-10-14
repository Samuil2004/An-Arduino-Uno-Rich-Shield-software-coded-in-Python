import csv
import datetime
import random 
import time
from flask import Flask, render_template, request, redirect,jsonify



app = Flask(__name__)
temperature_data = []
average_temperature = []

@app.route('/', methods=['GET','POST'])
def index():
    global temperature_data,average_temperature

    if request.method == 'POST':
        row = request.get_json()
        temperature_data.append(row)
        temperature_data = temperature_data[-15:]
        average_temperature.append(row[2])


    avrgtemp = round(sum(average_temperature)/len(average_temperature),2)

    return render_template('brandnew..html', temperature_data=temperature_data, average = avrgtemp )

if __name__ == '__main__':
    app.run(debug=True)
