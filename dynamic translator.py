
import urllib.request
from bs4 import BeautifulSoup
from translate import Translator
import spacy
import pandas as pd



nlp_ru = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/ru_core_news_sm/ru_core_news_sm-3.7.0')
nlp_en = spacy.load('/home/user/anaconda3/lib/python3.11/site-packages/en_core_web_sm/en_core_web_sm-3.7.1')
translator = Translator(from_lang="en", to_lang="ru")

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = "https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python"
headers={'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)

data = response.read()
soup = BeautifulSoup(data, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines

translated_text = ""

for texty in chunks:
    if texty:
        print (texty)
        tranlation = translator.translate(texty)
        translated_text = translated_text + tranlation

print(translated_text)
#по сути, все что мне нужно для перевода -  НЛП для распознавания голоса
#Обучить машину переводить текст. В пизду. Половину апишек - платная. А половина с ограничениями.
#Либо пользоваться гугл переводчиком(только эта хуйня может к хуям тебя забанить. Ы-ы-ы
# Переводчик, что будет переводить нужную для меня шнягу
# Штука, что будет воспроизводить текст при помощи голоса. Шняги по голосу уже есть в большом
# количестве. Так что юзнуть какую-нибудь бесплатную библеотеку - будет весело.
# Ебануть подобие апишки, рофла ради
#Да сделать так, чтобы оно трогало только чужую речь, разделяла речи по их тембру, воспроизводила
# после на выбранном языке или том на котором сейчас говорили. После друг друга или до - хз

#Прочитать текст с экрана(Можно пиздить из html)
#Определить язык\перевести
#Попробовать вывести\заменить текст на сайте - файле, либо ебануть
#по кордам текста штуки, что нужно.
#
#
