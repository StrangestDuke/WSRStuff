import pandas as pd
import yaml
import json
import re

irisdf = pd.read_csv('files to parse/apple_quality.csv')

irisdf = irisdf.loc[(irisdf.Quality == "good") & (irisdf.Sweetness >= 5.0)]

print(irisdf.describe())
for index, row in irisdf.iterrows():
    if row.Size >= -1.0:
        print("Awesome apple")

irisdf["Total"] = irisdf["Sweetness"] + irisdf["Juiciness"] + irisdf["Ripeness"]\
                  + irisdf["Crunchiness"]+ irisdf["Weight"] + irisdf["Size"]
print(type(irisdf))

irisdf = irisdf.loc[irisdf["Size"] >= -1.0, 'Juiciness'] = 5

print(type(irisdf))

irisdf.reset_index(drop=True, inplace=True)
with open('anaconda-project.json', 'w') as file:
    documents = json.dump(irisdf.to_dict(orient="records"), file, indent=2)

# If you would need something to disassemble a text - you can use regex