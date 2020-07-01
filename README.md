# trainWord2Vec_WikiCorpus
使用英文维基百科训练一个word2vec模型，并对其进行评估
## 数据处理
### 数据来源
训练词向量的第一步是取得一个合适的数据集。word2vec是基于非监督式学习的，所以一般情况下我们需要数据集语料越大越全的，这样才会训练出一个较为理想的模型。挑选数据集是维基百科定期更新语料。选择下载的是
**pages-articles.xml.bz2结尾的数据集**（*注意：不是pages-articles-multistream.xml.bz2 结尾的数据集*），否则在处理时会出现一些异常而无法解析。该数据集使用原生链接下载非常慢，推荐使用**迅雷工具下载**(大约一小时左右)

本教程使用gensim来训练word2vec模型，gensim作用主要分
- 分词好的句子作为输入
- 使用gensim的Word2Vec训练词向量

首先安装好gensim，在anaconda prompt使用命令行
```
pip install --upgrade gensim
```
出现以下successfully built smart open则为成功


### 数据处理
> 将XML文件转换为Text格式，使用gensim.corpora中的WikiCorpus函数来处理，具体方法是get_texts( )

process_wiki.py

- get_texts()：迭代每一篇文章，返回一个tokens list
- WikiCorpus，wiki数据的抽取处理类，能对下载的数据（articles.xml.bz2）进行抽取处理，得到纯净的文本语料。
 
在处理数据 分钟后（i7-8550U & 16G），得到 G的wiki.en.text文件

```
2020-07-01 05:15:28,836: INFO: running process_wiki.py enwiki-20200620-pages-articles.xml.bz2 wiki.en.text
C:\Users\baiyo\anaconda3\lib\site-packages\gensim\utils.py:1268: UserWarning: detected Windows; aliasing chunkize to chunkize_serial
  warnings.warn("detected %s; aliasing chunkize to chunkize_serial" % entity)
2020-07-01 05:17:04,298: INFO: Saved 10000 articles
2020-07-01 05:18:30,749: INFO: Saved 20000 articles
....
2020-07-01 09:13:15,599: INFO: Saved 4850000 articles
2020-07-01 09:13:44,882: INFO: Saved 4860000 articles
2020-07-01 09:13:47,866: INFO: finished iterating over Wikipedia corpus of 4860724 documents with 2755160976 positions (total 20358442 articles, 2827402342 positions before pruning articles shorter than 50 words)
2020-07-01 09:13:47,998: INFO: Finished Saved 4860724 articles
```