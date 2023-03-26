
from django.http import HttpResponse
from collections import Counter

from konlpy.tag import Okt, Komoran, Kkma, Hannanum, Twitter


import warnings

warnings.filterwarnings('ignore')


# 여기로 일기 리퀘스트를 보내면, 형태소로 다 잘라준다.
def korean_repeat(request):
    komoran = Komoran()
    # 파일을 읽어오면, 제일 많이 반복된 단어를 komoran이 읽어준다.
    # print(komoran.morphs("이경연 바보멍청이 정말루 바보"))

    twitter = Twitter()
    with open('yeoncrawl/doc/klaw.txt', 'r', encoding='utf-8') as dong_file:
        text = dong_file.read()
        twitpos = twitter.nouns(text)
        counts = Counter(twitpos)
        tags = counts.most_common(3)
        print(tags)
        return HttpResponse(tags)
