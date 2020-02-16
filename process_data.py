import pandas as pd
import json
import ast

df = pd.read_csv("data.csv")

def clean_des(x):
    json_data = x
    json_data = ast.literal_eval(json_data)
    x = json_data['code']
    print(x)
    return x

des = ["origin","destination"]
for d in des:
    try:
        df[d] = df[d].apply(clean_des)
    except:
        print("already clean {}".format(d))
df.to_csv("data.csv")