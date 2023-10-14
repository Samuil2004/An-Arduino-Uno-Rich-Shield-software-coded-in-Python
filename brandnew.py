import csv
import datetime
import random 
import time
from flask import Flask
from flask import render_template



csv_file = "subpointB.csv"
columns = ["Date" '\t''\t' "Time" '\t''\t'  "Temperature" '\t''\t' "Average Temperature" ]
sample_list = []

def time_printer():
    current_datetime = datetime.datetime.now()
    time1 = current_datetime.time()
    ftime = time1.strftime("%H:%M:%S")
    sample_list.append(ftime)
    return ftime

def date_printer():
    current_datetime = datetime.datetime.now()
    datetd = current_datetime.date()
    datenow = datetd.strftime("%m/%d/%Y")
    # sample_list.append(datenow)
    return datenow

def temperature_printer():
    temperature = random.randint(5,45)
    sample_list.append(temperature)
    return temperature


with open(csv_file, mode ='w', newline = '') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='\t')
        csv_writer.writerow(columns)
        # csv_writer.writerow(temp_list)
        # sample_list.append(avrg)
        # for row in sample_list:
        #     csv_writer.writerow(row)
        # sample_list.append(stravg)
        for i,row in enumerate(sample_list):
            csv_writer.writerow(row)
            # if i == 0:
            #     csv_writer.writerow(stravg)


app = Flask(__name__)

# columns = ["Date" '\t''\t' "Time" '\t''\t'  "Temperature" '\t''\t' "Average Temperature" ]
# sample_list = []
temp_list = []
listlen = 15
# csv_file = "subpointB.csv"


# def time_printer():
#     current_datetime = datetime.datetime.now()
#     time1 = current_datetime.time()
#     ftime = time1.strftime("%H:%M:%S")
#     sample_list.append(ftime)
#     return ftime

# def date_printer():
#     current_datetime = datetime.datetime.now()
#     datetd = current_datetime.date()
#     datenow = datetd.strftime("%m/%d/%Y")
#     # sample_list.append(datenow)
#     return datenow

# def temperature_printer():
#     temperature = random.randint(5,45)
#     sample_list.append(temperature)
#     return temperature

# with open(csv_file, mode ='w', newline = '') as csvfile:
#         csv_writer = csv.writer(csvfile, delimiter='\t')
#         csv_writer.writerow(columns)
#         # csv_writer.writerow(temp_list)
#         # sample_list.append(avrg)
#         # for row in sample_list:
#         #     csv_writer.writerow(roßw)
#         # sample_list.append(stravg)
#         for i,row in enumerate(sample_list):
#             csv_writer.writerow(row)
#             # if i == 0:
#             #     csv_writer.writerow(stravg)


@app.route('/', methods = ['POST'])
def index2():
    global sample_list
    sample = []
    sample = sample_list
    return render_template('brandnew..html', sample)



# def temperature_printer():
#     temperature = random.randint(5,45)
#     return temperature


# @app.route('/')
# def index():
#     global sample_list
#     global temp_list
#     ctime = time_printer()
#     temp = temperature_printer()
#     date1 = date_printer()
#     sample_list.append((date1,ctime,temp))
#     sample_list = sample_list[-listlen:]
#     temp_list.append(temp)
#     avrg = round(sum(temp_list)/len(temp_list),2)
#     stravg = str(avrg)
#     with open(csv_file, mode ='w', newline = '') as csvfile:
#         csv_writer = csv.writer(csvfile, delimiter='\t')
#         csv_writer.writerow(columns)
#         # csv_writer.writerow(temp_list)
#         # sample_list.append(avrg)
#         # for row in sample_list:
#         #     csv_writer.writerow(row)
#         # sample_list.append(stravg)
#         for i,row in enumerate(sample_list):
#             csv_writer.writerow(row)
#             if i == 0:
#                 csv_writer.writerow(stravg)

#             # csv_writer.writerow
#     # time.sleep(1)
#     return render_template('brandnew..html', sample = sample_list, average = avrg)


#         # ctime = time_printer()
#         # temp = temperature_printer()
#         # date1 = date_printer()
#         # sample_list.append((date1,ctime,temp))
#         # sample_list = sample_list[-listlen:]

        



# if __name__ == '__main__':
#     app.run(debug= True)




