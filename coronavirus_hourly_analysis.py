import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime
from os.path import isfile

filename="cases.csv"
df = pd.read_csv(filename,index_col=[0,1])

print(df)

new_df = df.filter(col for col in df.columns if '3pm' in col)

print(new_df)