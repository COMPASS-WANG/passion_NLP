#!/usr/bin/python
#-*- coding: utf-8 -*-
import jieba
import gensim.models.word2vec as w2v

# coding:utf8
# 读取倚天屠龙记文本，转码后存在新的文件里
fin = open('倚天屠龙记.txt', 'r')
fou = open('倚天屠龙记_uft8.txt', 'w')
line = fin.readline()
while line:
    newline = line.decode('GB18030').encode('utf-8')  # 用GBK、GB2312都会出错
    #print newline,
    print >> fou, newline,
    line = fin.readline()
fin.close()
fou.close()

fin = open('倚天屠龙记_uft8.txt', 'r')
fou = open('倚天屠龙记_segmented.txt', 'w')
print 'finish decode'

line = fin.readline()
while line:
    newline = jieba.cut(line, cut_all=False)
    str_out = ' '.join(newline).encode('utf-8').replace(',',' ').replace('。',' ').replace('？',' ').replace('！',' ') \
        .replace('“', ' ').replace('”',' ').replace('：',' ').replace('‘',' ').replace('’',' ').replace('-',' ') \
        .replace('（', ' ').replace('）',' ').replace('《',' ').replace('》',' ').replace('；',' ').replace('.',' ') \
        .replace('、', ' ').replace('…',' ')
    #print str_out
    print >> fou, newline,
    line = fin.readline()
fin.close()
fou.close()
print 'finish segment'

model_file_name = '倚天屠龙记_model.txt'
# 模型训练，生成词向量
sentences = w2v.LineSentence('倚天屠龙记_segmented.txt')
model = w2v.Word2Vec(sentences, size=20, window=5, min_count=5, workers=4)

model.save(model_file_name)
print 'finish training'

print model.similarity('赵敏'.decode('utf-8') ,'赵敏'.decode('utf-8') )
print model.similarity('周芷若'.decode('utf-8'),'赵敏'.decode('utf-8'),)
for k in model.similar_by_word('张三丰'.decode('utf-8')):
    print k[0], k[1]