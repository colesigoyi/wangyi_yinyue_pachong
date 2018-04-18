#!/usr/bin/env python

import requests
import json
from pyecharts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=a450002d7b0dcdd46dcb18ae3b1ebbf2'

headers = {
    'User-Agent': '删除',
    'Host': 'music.163.com',
    'Origin': 'http://music.163.com',
    'Referer': 'http://music.163.com/song?id=551816010',
}

user_data = {
    'params': 'KIgNaQF+xpWo4lC8MHl7WGvWb5UJA+QZiyKj7f8LyQEw78rm9o9XYuqmFJxvv6oqvIcfhpruuKZn5jt0CQlkSMgc4LOFTFwxm0b9ePXchPEUCcD6bQ59LynXPrdIZhRxZE0xC4JmcZ0nxYXNHQR3INL3GgKdbIENrrAOHkhhv8IOqZ6cS8upOVdlkgNSMc81dbonTmy5R0PQKPxMxoJn7uwwUYvkTEoNR12TrFM8FFk=',
    'encSecKey': 'c97d18a0b36dc1911aad23bb0057841061c63119e83b9414877c438ee76eeeb11afa0f5f56140036d78d2ccf024edb8aeec7492cb22c248154bcb07bed3b8627d8dfe6fd5bccfab780738cf5a88b32582c45bee0f15b96188c033abfc300e176c89eb0c5e80b52caa06ce39f203d83297981761fe347227812833649d52603ac',
}

response = requests.post(url,headers=headers,data=user_data)

data = json.loads(response.text)
hotcomments = []
for hotcommment in data['hotComments']:
    item = {
        'nickname':hotcommment['user']['nickname'],
        'content':hotcommment['content'],
        'likedCount':hotcommment['likedCount'],
    }
    hotcomments.append(item)

content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]

from pyecharts import Bar
bar = Bar("热评中点赞示例图")
bar.add("点赞数",nickname,liked_count, is_stack=True,make_line=["min","max"],mark_point=["average"])
bar.render()

from wordcloud import WordCloud
import matplotlib.pyplot as plt
content_text = " ".join(content_list)
wordcloud = WordCloud(font_path=r"/Users/删除/wordcloud_font/simhei.ttf",max_words=300).generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
wordcloud.to_file('test_wordcloud.png')
