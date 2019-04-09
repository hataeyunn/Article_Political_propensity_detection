from newspaper import Article
from konlpy.tag import Kkma, Okt
from konlpy.tag import Twitter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np



class SentenceTokenizer(object):
    def __init__(self):
        self.kkma = Kkma()
        self.okt = Okt()
        # stopwords = 의미 없는 단어들
        self.stopwords = ['중인', '만큼', '마찬가지', '꼬집었', "연합 뉴스", "데일리", "동아일보", "중앙일보", "조선일보", "기자"
            , "아", "휴", "아이구", "아이쿠", "아이고", "어", "나","연합","자료사진", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가", ]

    def url2sentences(self, url):
        article = Article(url, language='ko')
        article.download()
        article.parse()
        sentences = self.kkma.sentences(article.text)

        for idx in range(0, len(sentences)):
            if len(sentences[idx]) <= 10:
                sentences[idx - 1] += (' ' + sentences[idx])
                sentences[idx] = ''

        return sentences

    def text2sentences(self, text):
        sentences = self.kkma.sentences(text)
        for idx in range(0, len(sentences)):
            if len(sentences[idx]) <= 10:
                sentences[idx - 1] += (' ' + sentences[idx])
                sentences[idx] = ''

        return sentences

    def get_nouns(self, sentences):
        nouns = []
        for sentence in sentences:
            if sentence is not '':
                nouns.append(' '.join([noun for noun in self.okt.nouns(str(sentence))
                                       if noun not in self.stopwords and len(noun) > 1]))

        return nouns


class GraphMatrix(object):
    def __init__(self):
        self.tfidf = TfidfVectorizer()
        self.cnt_vec = CountVectorizer()
        self.graph_sentence = []

    def build_sent_graph(self, sentence):
        tfidf_mat = self.tfidf.fit_transform(sentence).toarray()
        self.graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
        return self.graph_sentence

    def build_words_graph(self, sentence):
        cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
        vocab = self.cnt_vec.vocabulary_
        return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word]: word for word in vocab}
