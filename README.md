#조선대학교 2021년도 1학기 캡스톤디자인 프로젝트입니다.

##주제 : 국민청원 2차 분류 모델 개발

내용 :

국민청원은 기본적으로 1차 카테고리로 분류 되어 있습니다. ( 미래, 반려동물, 일자리 등 )

이 경우 원하는 청원에 접근하기 위해서는 1차 카테고리를 지정 한 뒤 일일이 찾아봐야 하는 어려움이 있습니다.

저희는 국민청원에 1차 카테고리 별로 2차 카테고리를 분류하기 위해 다음과 같은 절차를 거쳐 개발할 예정입니다.

1. 데이터 수집 [ 완료 ]

국민청원 사이트에서 관련 데이터를 크롤링합니다. lovit님의 국민청원 데이터에 이어 자체적인 크롤링을 진행합니다.

2. 데이터 전처리 [ 완료 ]

단어가 많을 경우 이후에 처리하는 문장의 벡터를 얻는 작업에서 어려움이 있을 수 있습니다. ( 현재 단어 벡터의 평균을 문장의 벡터로 사용 중 )

그러므로 단어가 너무 많이 포함 된, 즉 이상치라고 생각 될 정도의 긴 청원과 너무 적은 청원을 제거하는 작업을 진행합니다.

또한 데이터를 통계적으로 살펴보는 시간을 가질 예정입니다.

3. 텍스트 임베딩 [ 완료 ]

텍스트 데이터를 수치화하기 위해 임베딩 과정을 거칩니다. 이 과정에서 문장을 단어별로 구분하여 단어의 벡터를 구하게 됩니다.

임베딩 방식은 FastText의 Unsupervised learning을 사용합니다.

이유로는 국민청원은 SNS의 자연어와 같이 일반인이 작성하는 글로 예외가 되는 단어가 등장 할 확률이 높습니다. 그러므로 OOV문제를 해결하기 위해 이러한 방법을 사용합니다.

또한 BagOfWords 방식을 사용하지 않는 이유는 유사한 단어는 분류를 하는 과정에서 가능한 유사하게 분류하기 위해서입니다.

이 내용은 Word2Vec과 유사한 방법이기 때문이며 제 블로그를 보시면 조금 이해하실 수 있으실 것이라 생각됩니다.

4. 문장 벡터 [ 완료 ]

문장 벡터는 단어의 벡터를 평균내는 방법을 이용하여 구현하였습니다.

단어가 많이 포함되어 있을수록 문장의 벡터를 구할 때 흔들릴 가능성이 높습니다.

[ 그림 추가 하자! ( 왜 흔들릴 수 있는지? ) ]

방식은 다음과 같습니다.

[ 그림 추가 하자! ( 구하는 방식 numpy를 이용하여 열 단위로 평균을 내는 소스도? ) ]

최대한 벡터의 흔들림 현상을 줄이기 위해서 가능한 벡터의 크기를 크게 만들었습니다.

현재 문장을 200차원으로 임베딩함으로써 데이터의 수에 대비해서 조금 더 여유롭게 설정하였습니다. 차원이 높다고하여 분류가 잘 된다는 혹은 효과적이라고 말할 수 없지만 데이터 사이가 조금 더 독립성을 가진다는 특징이 더해집니다.

5. 데이터 군집화 [ 완료 ]

다음으로는 텍스트 데이터를 군집화하는 과정입니다.

데이터를 군집화 한 이유로는 데이터를 라벨링하기 위해서 입니다. 2차 카테고리를 분류하기 위해서는 관련된 라벨이 있어야 합니다.

그러한 이유로 데이터를 군집하여 유사한 문장이 모여있는 군집을 기반으로 2차 카테고리를 군집화하였습니다.

수십만개의 문장이지만 각 카테고리를 250개의 군집으로 묶어서 확인함으로써 실제로 라벨링 하는 과정을 간소화 시켰습니다.

6. 데이터 라벨링 [ 현재 진행 중 ]

군집을 기준으로 데이터를 라벨링 하는 과정입니다.

추후 완료 시 설명을 적겠습니다.





