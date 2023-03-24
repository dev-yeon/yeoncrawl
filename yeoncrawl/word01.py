
from wordcloud import  WordCloud
from konlpy.tag import Komoran
from collections import Counter
import numpy as np
from PIL import Image

text = open ('doc.klaw.txt', encoding='utf-8').read()

# Komoran 함수를 이용해 형태소 분석

komoran = Komoran()

line = []
line = []
line = komoran.pos(text)

n_adj =[]
# 명사와 동사 만 n_adhj에 넣어주기
for word, tag in line:
    if tag in ['NNG','NNP','NNB','VV','VA']:
        n_adj.append(word)

# 제외할 단어 추가 (를과 의를 삭제함 )
stop_words = "를 의 "
stop_words = set(stop_words.split(' '))

# 불용어를 제외한 단어만 남기기
n_adj= [word for word in n_adj if not word in stop_words]

#가장 많이 나온 단어 50개 저장
count = Counter(n_adj)
tags = count.most_common(50)
print(tags)

# wordCloud를 생성한다
# 마스크 이미지로

mask = Image.new("RGBA", (424, 369), (255, 255, 255))
image = Image.open('img.book.jpeg').convert("RGBA")
x,y = image.size
mask.paste(image,(0, 0, x, y), image)
mask = np.array(mask)

# 한글을 분석하기 위해 font를 한글로 지정해 주어야 한다.
wc = WordCloud(font_path='font.d2.ttf', background_color='white')
