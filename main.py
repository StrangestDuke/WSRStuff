
import pandas as pd
import json
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import spacy
from spacypdfreader.spacypdfreader import pdf_reader

#Geting chuncks of code
np.set_printoptions(threshold=4000)
irisdf = pd.DataFrame(columns=pd.read_csv('files to parse/apple_quality1.csv').columns)
for irisd in pd.read_csv('files to parse/apple_quality1.csv', chunksize=1000):
    irisdf = pd.concat([irisdf, irisd])

#Saving stuff by the sweetness
df = irisdf.drop(["Acidity", "Quality"], axis=1)
testing = df.groupby(["Sweetness"]).mean().sort_values('Size', ascending=True)
irisdf.reset_index(drop=True, inplace=True)
with open('Apples_Grouped_By_Sweetness.json', 'w') as file:
    documents = json.dump(testing.to_dict(orient="records"), file, indent=2)


#Making it to appear only good and converting it to normal values
irisdfgood = irisdf.loc[(irisdf.Quality == "good")]

irisdfgood.reset_index(drop=True, inplace=True)
acidity_in_list =[]
i = 0
for number_of_acidity in irisdfgood.Acidity:
    acidity_in_list.append(float(number_of_acidity))
    i += 1
#irisdf_good_n_clean = irisdf.loc[irisdf["Acidity"], ["Acidity"]] = acidity_in_list
irisdf_clean = irisdf.drop(["Acidity","Quality"], axis=1)
#Setting up colors
xs = np.arange(10)
ys = [i+xs+(i*xs)**2 for i in range(10)]
colors = iter(cm.rainbow(np.linspace(0, 1, len(ys))))

#Taking columns out the file
columns = pd.DataFrame(columns=pd.read_csv('files to parse/apple_quality1.csv').columns)
del columns["Acidity"], columns["Quality"], columns['A_id']

print(irisdf_clean.describe())

with open('anaconda-project.json', 'w') as file:
    documents = json.dump(irisdf_clean.to_dict(orient="records"), file, indent=2)
#А ведь я могу попробовать на графике запустить bad apple
#Making graphic

#Сладость почти равняется размеру(зависит)
#Сладость от веса немного зависит
#Чем больше хруст яблока, тем более оно сладкое, такая же штука с сочностью яблока и зрелостью

#Расчет этой хуйни займёт очень огромное время.

#В юпитерском ноутбуке, можно смачно взять граф. Через мат либ ебануть простенький
#граф и через скатер надристать точками с маркером "dick" на японском


#for number in irisdf_good_n_clean.Sweetness:
#    y.append(float(number))
#for column in columns:
#    plt.legend(str(column))
#for column in columns:
#    if column != "A_id":
#        for number in irisdf_good_n_clean[column]:
#            x.append((float(number)*333.3))
#    else:
#        for number in irisdf_good_n_clean[column]:
#            x.append(float(0))
#    color_that_we_are_using = next(colors)
#    sns.histplot(x,color=color_that_we_are_using, kde=False, bins=np.arange(xmin, xmax,width))
#
#    x.clear()
#plt.legend()
#plt.show()

#Doing total of all numbers
irisdf["Total"] = irisdf["Sweetness"] + irisdf["Juiciness"] + irisdf["Ripeness"]\
                  + irisdf["Crunchiness"]+ irisdf["Weight"] + irisdf["Size"]



# If you would need something to disassemble a text - you can use regex