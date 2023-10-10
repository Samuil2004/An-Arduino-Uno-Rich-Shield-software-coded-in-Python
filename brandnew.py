import csv
import datetime
import random 
import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

columns = ["Date" '\t''\t' "Time" '\t''\t'  "Temperature" '\t''\t' "Average Temperature" ]
sample_list = []
temp_list = []
listlen = 15
csv_file = "subpointB.csv"


def time_printer():
    current_datetime = datetime.datetime.now()
    time1 = current_datetime.time()
    ftime = time1.strftime("%H:%M:%S")
    return ftime

def date_printer():
    current_datetime = datetime.datetime.now()
    datetd = current_datetime.date()
    datenow = datetd.strftime("%m/%d/%Y")
    return datenow

def temperature_printer():
    temperature = random.randint(5,45)
    return temperature



@app.route('/')
def index():
    global sample_list
    global temp_list
    ctime = time_printer()
    temp = temperature_printer()
    date1 = date_printer()
    sample_list.append((date1,ctime,temp))
    sample_list = sample_list[-listlen:]
    temp_list.append(temp)
    avrg = round(sum(temp_list)/len(temp_list),2)
    with open(csv_file, mode ='w', newline = '') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='\t')
        csv_writer.writerow(columns)
        for i,row in enumerate(sample_list):
            csv_writer.writerow(row)
            if i == 0:
                csv_writer.writerow("","",avrg)

            # csv_writer.writerow
    # time.sleep(1)
    return render_template('brandnew..html', sample = sample_list, average = avrg)


        # ctime = time_printer()
        # temp = temperature_printer()
        # date1 = date_printer()
        # sample_list.append((date1,ctime,temp))
        # sample_list = sample_list[-listlen:]

        



if __name__ == '__main__':
    app.run(debug= True)




