import requests
import json
import pandas as pd

df = pd.read_json("http://localhost:3030/flights?date=2020-01-01")
df.to_csv('data.csv', mode='a', header=True)

months = range(1,13)
days = range(1,30)

for month in months:
    for day in days:
        if int(month) < 10 :
            m = "0" + str(month)
        if int(day) < 10:
            d = "0" + str(day)
        df = pd.read_json("http://localhost:3030/flights?date=2020-{}-{}".format(m,d))
        df.to_csv('data.csv', mode='a', header=False)

