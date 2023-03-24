from wordcloud import WordCloud  #  - 이 패키지는 말그대로 워드클라우드를 생성에 필요한 기본 모듈입니다.
import matplotlib.pyplot as plt  # - 생성한 워드클라우드 데이터를 시각화하여 그리기 위해 불러옵니다.
from collections import Counter   # - 텍스트를 추출하고, 빈도 수를 추출하기 위해 사용합니다. 기본적으로 워드클라우드는 단어의 출현 빈도가 클수록 더 크게 그려집니다.
from konlpy.tag import Okt   #- 한국어를 처리하는 대표적인 형태소 분석 패키지입니다. Okt, Kkma 등 여러가지 패키지들이 존재하는데 형태소 분석기마다 명사, 명사 등의 형태소를 조금씩 다르게 처리하므로 다양하게 사용해본 후, 가지고 있는 문서 특성에 적합한 형태소 분석기를 사용하는 것이 좋습니다.
from PIL import Image   # - 워드클라우드를 원하는 형태로 그리기 위해 그림을 불러오는 패키지입니다.
import numpy as np    #  - 불러온 그림을 배열로 나타내어 쉽게 처리할 수 있도록 도와주는 패키지입니다.


with open('대한민국헌법.txt', 'r', encoding='utf-8') as f:
    text = f.read()

okt = Okt()
nouns = okt.nouns(text) # 명사만 추출

words = [n for n in nouns if len(n) > 1]   # 단어의 길이가 1개인 것은 제외

c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함
# 한글로 워드 클라우드 시각화
wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
plt.figure()
plt.imshow(gen)

wc.to_file('법전_워드클라우드.png')
