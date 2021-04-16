### FastText 

## 실행파일 준비

#git clone https://github.com/facebookresearch/fastText.git

#cd fastText

#make


## 단어벡터 학습

# ./fastText/fasttext -input data.txt -output data.model

# -dim, -ws, -minCount를 통해서 파라미터 값을 설정한다.

## 벡터 확인하기

# most_similar.py를 통해서 '영화'라는 단어와 가장 유사한 벡터 30개를 뽑아낸다
