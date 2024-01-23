import pandas as pd
import yaml

irisdf = pd.read_csv('files to parse/apple_quality.csv')

irisdf = irisdf.loc[(irisdf.Quality == "good") & (irisdf.Sweetness >= 5.0)]

print(irisdf.columns)