# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
fn='travel.txt'

with open(fn,'r',encoding='utf-8') as fb:
    
    data=fb.read()
    
cut_txt=''.join(jieba.cut(data))

#print(cut_txt)
 

wd=WordCloud(
    font_path='C:/Windows/Fonts/mingliu',
    background_color='black',width=800,height=600).generate(cut_txt)

plt.imshow(wd)

plt.axis('off')

wd.to_file('詞雲圖.png')
    
'''
img1=wd.to_image()

img1.show(wd, interpolation="bilinear")
'''




