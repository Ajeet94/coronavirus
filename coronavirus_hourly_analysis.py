import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime
from os.path import isfile

filename="cases.csv"
df = pd.read_csv(filename,index_col=[0,1])

print(df)

# new_df = df.filter(col for col in df.columns if '3pm' in col)

# print(new_df)

# def get_url_resp(country="Worldwide"):
#     base_url = "https://www.worldometers.info/coronavirus/"
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
#     if country =="Worldwide":
#         url = base_url
#     else:
#         url =base_url+"country/"+country+"/"
#     response = requests.get(url, headers = headers)
#     html = response.text
#     soup = BeautifulSoup(html,"html.parser")
#     # a = soup.find_all("script")
#     a = soup.select(".col-md-6")
#     # print(a)
  
#     if country =="Worldwide":
#         return [a[2].find_all(type="text/javascript")[0],a[3].find_all(type="text/javascript")[0]]
#     else:
#         return [a[0].find_all(type="text/javascript")[0],a[1].find_all(type="text/javascript")[0]]

# a = get_url_resp()#'US')

# d = a[0].get_text().rsplit("categories",1)[1].split("[")[1].split("]")[0]
# b = a[0].get_text().rsplit("data",1)[1].split("[")[1].split("]")[0]
# c=b.split(',')
# e=d.split(',')
# lst=[]
# for i in range(len(c)):
#     lst.append(int(c[i]))

# lst_date = []
# for i in e:
#     lst_date.append(i.replace('"',''))

# print(dict(zip(lst_date,lst)))
