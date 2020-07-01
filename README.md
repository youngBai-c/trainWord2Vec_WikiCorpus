# trainWord2Vec_WikiCorpus
使用英文维基百科训练一个word2vec模型，并对其进行评估
## 环境
- （Intel(R) Core(TM) i7-8550U & 16G）
- Anaconda 3.1
- gensim

## 获取语料


训练词向量的第一步是取得一个合适的数据集。word2vec是基于非监督式学习的，所以一般情况下我们需要数据集语料越大越全的，这样才会训练出一个较为理想的模型。挑选数据集是维基百科定期更新语料。选择下载的是
**pages-articles.xml.bz2结尾的数据集**（*注意：不是pages-articles-multistream.xml.bz2 结尾的数据集*），否则在处理时会出现一些异常而无法解析。该数据集使用原生链接下载非常慢，推荐使用**迅雷工具下载**(大约一小时左右)

下载等待的时间，首先安装好gensim，本教程使用gensim来训练word2vec模型。在anaconda prompt使用命令行：
```
pip install --upgrade gensim
```
出现以下successfully built smart open则为成功



维基百科语料下载完成，得到的是一份xml文件，不用担心怎么使用，gensim内置的WikiCorpus类可以方便提取
文章的标题与内容。具体方法是get_texts( )

process_wiki.py

- get_texts()：迭代每一篇文章，返回一个tokens list
- WikiCorpus，wiki数据的抽取处理类，能对下载的数据（articles.xml.bz2）进行抽取处理，得到纯净的文本语料。
 


```
2020-07-01 09:49:33,419: INFO: running process_wiki.py enwiki-20200620-pages-articles.xml.bz2 wiki.en.txt
C:\Users\baiyo\anaconda3\lib\site-packages\gensim\utils.py:1268: UserWarning: detected Windows; aliasing chunkize to chunkize_serial
  warnings.warn("detected %s; aliasing chunkize to chunkize_serial" % entity)
2020-07-01 09:51:08,201: INFO: Saved 10000 articles
2020-07-01 09:52:34,478: INFO: Saved 20000 articles
....
2020-07-01 14:03:58,727: INFO: Saved 4850000 articles
2020-07-01 14:04:28,322: INFO: Saved 4860000 articles
2020-07-01 14:04:31,335: INFO: finished iterating over Wikipedia corpus of 4860724 documents with 2755160976 positions (total 20358442 articles, 2827402342 positions before pruning articles shorter than 50 words)
2020-07-01 14:04:31,475: INFO: Finished Saved 4860724 articles
```

## 词向量训练

## 词向量实验

## Note

处理数据：大约 小时后，得到 G的wiki.en.txt文件
训练模型： 