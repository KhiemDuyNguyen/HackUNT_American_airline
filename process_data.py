import pandas as pd
import json
import ast

df = pd.read_csv("data.csv")

# Clean json file into readable dict python data type, filter airport code only
def desC(x):
    json_data = ast.literal_eval(x)
    return json_data['code']

# Clean flight duration
def durationC(x):
    json_data = ast.literal_eval(x)
    print(json_data['hours'])
    return int(json_data['hours'])*60 + int(json_data['minutes'])

def modelC(x):
    json_data = ast.literal_eval(x)
    return json_data['model']
def capacityC(x):
    json_data = ast.literal_eval(x)
    print(json_data)
    json_data2 = json_data['passengerCapacity']
    print(json_data2['total'])
    return json_data2['total']
def speedC(x):
    json_data = ast.literal_eval(x)
    return json_data['speed']

des = ["origin","destination"]
for d in des:
    try:
        df[d] = df[d].apply(desC)
    except:
        print("already clean {}".format(d))

try:
    df["duration"] = df["duration"].apply(durationC)
except:
    print("already clean duration")

try:
    df["model"] = df["aircraft"].apply(modelC)
except:
    print("already clean aircraft model")

try:
    df["MaxCapa"] = df["aircraft"].apply(capacityC)
except:
    print("already clean capacity")
try:
    df["speed"] = df["aircraft"].apply(speedC)
except:
    print("already clean speed")

df.to_csv("data.csv")