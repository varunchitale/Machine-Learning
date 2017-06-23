import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities
from gensim.models import Word2Vec as w2v

data = pd.read_csv("jokes.csv")
ques = data['Question'].values.tolist()
ans  = data['Answer'].values.tolist()

corpus = ques + ans

tok_corpus = [nltk.word_tokenize(sent.decode('utf-8')) for sent in corpus]

#model = gensim.models.Word2Vec(tok_corpus, min_count=1, size=32)
#model.save('model1_word2vec')
model = w2v.load('model1_word2vec')
#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
print model.most_similar('hi')