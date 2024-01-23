import pandas as pd
import yaml

irisdf = pd.read_csv('files to parse/apple_quality.csv')

irisdf = irisdf.loc[(irisdf.Quality == "good") & (irisdf.Sweetness >= 5.0)]
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print(irisdf)
with open('anaconda-project.yml', 'w') as file:
    documents = yaml.dump(irisdf.to_dict(orient="records"), file, default_flow_style=False)