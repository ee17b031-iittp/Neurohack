import os
import warnings
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


warnings.filterwarnings(action = 'ignore')


def countvectorizer(corpus, stopwords, lowercase, ngram_range, max_features):
    vectorizer = CountVectorizer(stop_words=stopwords, lowercase=lowercase, 
    ngram_range=ngram_range, max_features=max_features)
    vectorizer.fit(corpus)
    return vectorizer

def tfidfvectorizer(corpus, stopwords, lowercase, ngram_range, max_features):
    vectorizer = TfidfVectorizer(stop_words=stopwords, lowercase=lowercase, 
    ngram_range=ngram_range, max_features=max_features)
    vectorizer.fit(corpus)
    return vectorizer

def word2vecmodel(corpus, stopwords, lowercase, skip_gram, vector_size, window_size):
    data = []
    # iterate through each sentence in the file
    for i in corpus:
        temp = []
        # tokenize the sentence into words
        for j in word_tokenize(i):
            if lowercase:
                if j.lower() not in stopwords:
                    temp.append(j.lower())
            else:
                if j not in stopwords:
                    temp.append(j)
        data.append(temp)
    model = Word2Vec(data, min_count=1, vector_size=vector_size, sg=skip_gram, window=window_size)
    return model

def glove
