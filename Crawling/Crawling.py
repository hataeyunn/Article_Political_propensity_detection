#-*- coding: utf-8 -*-
import networkx
from konlpy.tag import Komoran
import re
from newspaper import Article
from bs4 import BeautifulSoup
import urllib.request

def urlfromNaver(url):
    article = Article(url, language='ko')
    article.download()
    article.parse()
    contents = article.text

    for i in range(contents.count(("\n")) // 2):
        contents = contents[contents.index("\n") + 2:]
    return contents


def urlfromDaum(url):
    source_code_from_URL = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', attrs={'class':'article_view'}):
        for item in soup.find_all('p',attrs={'dmcf-ptype':'general'}):
            text = text + str(item.find_all(text=True))

    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\']',
                          '', cleaned_text)
    return cleaned_text


url1 = 'https://news.v.daum.net/v/20190514170803431'
url2 ='https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=025&aid=0002906783'




if('daum' in url1 ):
    print(urlfromDaum(url1))

print("\n\n")

if('naver' in url2 ):
    print(urlfromNaver(url2))





