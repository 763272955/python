#-*- coding: utf-8 -*-
import  nltk
import requests
import matplotlib
from nltk.corpus import  stopwords
from bs4 import BeautifulSoup
response = requests.get('http://php.net')
html = response.content
# print (html)
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)
# print (text)
tokens = [t for t in text.split()]
print (tokens)
sr = stopwords.words('english')
clean_tokens = []
for token  in tokens:
    if  token not in sr:
        clean_tokens.append(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print (str(key) + ':' + str(val))
    freq.plot(20,cumulative=False)

