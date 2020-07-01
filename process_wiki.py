#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Pan Yang (panyangnlp@gmail.com)
# Copyrigh 2017
 
from __future__ import print_function
 
import logging
import os.path
import six
import sys
 
from gensim.corpora import WikiCorpus
 
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0]) # 版本兼容性差异，以最新版本为主
    logger = logging.getLogger(program)  # 安装logging
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    # 检查和处理输入参数
    if len(sys.argv) != 3:
        print("Using: python process_wiki.py enwiki-20200620-pages-articles.xml.bz2 wiki.en.text")
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = " "
    i = 0
 
    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
    
        if six.PY3:
            output.write(str(b'', 'utf-8') + '\n')
        #   ###another method###
        #    output.write(
        #            space.join(map(lambda x:x.decode("utf-8"), text)) + '\n')
        else:
            output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")
 
    output.close()
    logger.info("Finished Saved " + str(i) + " articles")