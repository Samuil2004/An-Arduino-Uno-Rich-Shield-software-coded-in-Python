import csv
import datetime
import random 
import time
from flask import Flask, render_template, request, redirect,jsonify



app = Flask(__name__)
temperature_data = []
average_temperature = []
average_humidity = []
average_light = []


@app.route('/', methods=['GET','POST'])
def index():
    global temperature_data,average_temperature, average_humidity, average_light

    if request.method == 'POST':
        row = request.get_json()
        temperature_data.append(row)
        temperature_data = temperature_data[-15:]
        tr = float(row[2])
        average_temperature.append(tr)
        tw = float(row[3])
        average_humidity.append(tw)
        tm = int(row[4])
        average_light.append(tm)
    avrgtemp = round(sum(average_temperature)/len(average_temperature),2)

    return render_template('Mainpage.html', temperature_data=temperature_data, average = avrgtemp)

@app.route('/Temperatures.html', methods=['GET','POST'])
def Temperature():
    global average_temperature

    average_temperature.sort()
    min_temp = average_temperature[0]
    max_temp = average_temperature[-1]

    avrgtemp = round(sum(average_temperature)/len(average_temperature),2)
    return render_template('Temperatures.html',mintemp = min_temp,maxtemp = max_temp, average = avrgtemp)

@app.route('/Humidity.html', methods=['GET','POST'])
def Humidity():
    global average_humidity
    average_humidity.sort()

    min_hum = average_humidity[0] if average_humidity else 0  
    max_hum = average_humidity[-1] if average_humidity else 0  

    avrgtemp = round(sum(average_humidity)/len(average_humidity),2)
    return render_template('Humidity.html',mintemp = min_hum,maxtemp = max_hum, average = avrgtemp)



@app.route('/Light.html', methods=['GET','POST'])
def Light():
    global average_light
    average_light.sort()
    min_l = average_light[0]
    max_l = average_light[-1]

    avrgtemp = round(sum(average_light)/len(average_light),2)
    return render_template('Light.html',mintemp = min_l,maxtemp = max_l, average = avrgtemp)


if __name__ == '__main__':
    app.run(debug=True)
