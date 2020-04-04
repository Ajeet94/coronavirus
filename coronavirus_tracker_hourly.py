import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime
from os.path import isfile

def get_url_resp(country="Worldwide"):
    base_url = "https://www.worldometers.info/coronavirus/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
    if country =="Worldwide":
        url = base_url
    else:
        url =base_url+"country/"+country+"/"
    response = requests.get(url, headers = headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")

    return soup.find_all(class_="maincounter-number")

def get_number(country="Worldwide"):
    statuses = {
        "Cases":0,
        "Deaths":1,
        "Recovered":2
    }
    soup_numbers = get_url_resp(country)
    return {status:soup_numbers[statuses[status]].get_text().replace(" ","").replace(",","").replace("\n","") for status in statuses}

def get_current_datetime():
    current_datetime = datetime.datetime.utcnow()
    if current_datetime.hour <12:
        ampm ="am"
        if current_datetime.hour == 0:
            hour = str(12)
        else:
            hour=str(current_datetime.hour)
    else:
        ampm ="pm"
        if current_datetime.hour == 12:
            hour = str(12)
        else:
            hour=str(current_datetime.hour-12)

    current_hour = hour + ampm
    return str(current_datetime.date())+' '+current_hour+" GMT"

Countries = ("Worldwide","China","US","Italy","Spain","Germany","France","UK","India","South-Korea","Iran","Netherlands","Belgium","Switzerland","Turkey","Sweden","Indonesia","Portugal")
statuses_tuple = ("Cases","Deaths","Recovered")
current_datetime = get_current_datetime()

cases=[]
country_outside=[]
status_inside=[]
for country in Countries:
    numbers = get_number(country)
    for sta in statuses_tuple:
        cases.append(numbers[sta])
        country_outside.append(country)
        status_inside.append(sta)

hier_index = pd.MultiIndex.from_tuples(list(zip(country_outside,status_inside)))
df = pd.DataFrame(data=cases,index=hier_index,columns=[current_datetime])

filename="hourly cases.csv"
df_head=pd.read_csv(filename,nrows=0)
df_head_lst = list(df_head)[2:]
data_types = {val:pd.Int64Dtype() for val in df_head_lst}

if isfile(filename):
    df_old = pd.read_csv(filename,index_col=[0,1],dtype=data_types)
    new_df = df_old.join(df,how='outer')
else:
    new_df = df
new_df.to_csv(filename)