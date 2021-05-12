from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('data.model.vec')

print(model.most_similar('영화', topn=30))  #'영화'라는 단어와 가장 유사한 단어 30개
