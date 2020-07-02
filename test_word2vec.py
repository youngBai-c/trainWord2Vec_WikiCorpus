from pyemd import emd
import gensim
# import gensim.models import Word2Vec

# 模型读取方式
model = gensim.models.Word2Vec.load('C:\ProgramData\wordvec\word2vec.model');

# 查看词向量 | 维度
vec = model['man'];
print('man:',vec);
print('Shape:',vec.shape);
# man [ 2.21187860e-01  3.63909841e+00 ..... 
#      -7.56549418e-01 -2.68334198e+00] 250维向量

# 前N个最相似词
words = model.most_similar("queen");
print("The most similar words: ");
for w in words:
    print(w);
# The most similar words:

    
# 余弦相似度(w1,w2)
similar_rate = model.similarity("man","woman");
print(similar_rate);  
# 0.7089453

result = model.similar_by_word("cat");
print(result);
# ('dog', 0.755760908126831),

# 余弦相似度(v1,v2)
similar_rate = model.n_similarity(['sushi', 'shop'], ['japanese', 'restaurant']);
print(similar_rate);  
# 0.6058457

# 找不属于同一类的word
word = model.doesnt_match("woman man cat boy".split());
print(word);

# 词移动距离
sentence_obama = 'Obama speaks to the media in Illinois'.lower().split()
sentence_president = 'The president greets the press in Chicago'.lower().split()
dis = model.wmdistance(sentence_obama, sentence_president)
print(dis); 
# 23.09102023507841
