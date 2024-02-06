
import pandas as pd
import json
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import spacy

nlp_ger = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/de_core_news_sm/de_core_news_sm-3.7.0')

nlp_en = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/en_core_web_sm/en_core_web_sm-3.7.1')

with open("./files to parse/textindoc.doc", "r") as f:
    text_doc = f.read()

with open("./files to parse/cdowiki-20240120-pages-articles-multistream-index.txt", "r") as f:
    text_txt = f.read()

doc_txt = nlp_en(text_doc)

doc_doc = nlp_en(text_txt)

#по сути, все что мне нужно для перевода -  НЛП для распознавания голоса
# Переводчик, что будет переводить нужную для меня шнягу
# Штука, что будет воспроизводить текст при помощи голоса. Шняги по голосу уже есть в большом
# количестве. Так что юзнуть какую-нибудь бесплатную библеотеку - будет весело.
# Ебануть подобие апишки, рофла ради
#Да сделать так, чтобы оно трогало только чужую речь, разделяла речи по их тембру, воспроизводила
# после на выбранном языке или том на котором сейчас говорили. После друг друга или до - хз
