# trainWord2Vec_WikiCorpus
使用英文维基百科训练一个word2vec模型，并对其进行评估
## 数据处理
### 数据来源
训练词向量的第一步是取得一个合适的数据集。word2vec是基于非监督式学习的，所以一般情况下我们需要数据集语料越大越全的，这样才会训练出一个较为理想的模型。挑选数据集是维基百科定期更新语料。选择下载的是
pages-articles.xml.bz2结尾的数据集（注意：不是pages-articles-multistream.xml.bz2 结尾的数据集），否则在处理时会出现一些异常而无法解析。该数据集使用原生链接下载非常慢，推荐使用迅雷工具下载

首先安装好gensim，在anaconda prompt使用命令行
```
pip install --upgrade gensim
```
出现以下successfully built smart open则为成功


### 数据处理
