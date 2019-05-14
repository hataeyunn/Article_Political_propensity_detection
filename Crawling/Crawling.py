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

def urlfromHani(url):
    source_code_from_URL = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    text1 = ''
    for item in soup.find_all('div', attrs={'class':'text'}):
        text = text + str(item.find_all(text=True))

    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\']',
                          '', cleaned_text)
    while cleaned_text[0] is " ":
        cleaned_text = cleaned_text[1:]
    return cleaned_text

def urlfromChungang(url):
    article = Article(url, language='ko')
    article.download()
    article.parse()
    contents = article.text

    return contents

def urlfromChosun(url):
    source_code_from_URL = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', attrs={'class':'par'}):
        text = text + str(item.find_all(text=True))

    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\']',
                          '', cleaned_text)
    return cleaned_text


url = 'https://news.v.daum.net/v/20190514214820338'
url1 = 'https://news.v.daum.net/v/20190514170803431'
url2 ='https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=025&aid=0002906783'
url3 = 'http://www.hani.co.kr/arti/politics/politics_general/893614.html'
url4 = 'https://news.joins.com/article/23466283'
url5 = 'http://news.chosun.com/site/data/html_dir/2019/05/14/2019051403294.html'


###########test#######################
if('news.v.daum.net' in url1 ):
    print(urlfromDaum(url1))

print("\n\n")

if('news.naver.com' in url2 ):
    print(urlfromNaver(url2))

print("\n\n")

if('www.hani.co.kr' in url3):
    print(urlfromHani(url3))
print("\n\n")
if('news.joins.com' in url4):
    print(urlfromChungang(url4))
    
print("\n\n")
print(urlfromChosun(url5))



###### 구현 #################33333
if('news.naver.com' in url):
    contents = urlfromNaver(url)
elif('news.v.daum.net' in url):
    contents = urlfromDaum(url)
elif('www.hani.co.kr' in url):
    contents = urlfromHani(url)
elif('news.joins.com' in url):
    contents = urlfromChungang(url)
elif('http://news.chosun.com' in url):
    contents = urlfromChosun(url)

