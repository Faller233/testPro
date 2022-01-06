#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 计算相似度

import GlobalParament
import PreProcess
import MyModel
import numpy as np
from gensim.models.word2vec import Word2Vec
from gensim.models import word2vec

def calc_sim(model_path, train_path, test_sentence):
    model = Word2Vec.load(model_path)
    vocab = list(model.wv.index_to_key)
    # 改进
    # vocab = set(model.wv.vocab.keys())
    # print(len(vocab))
    # print(vocab[:20])
    # 计算相似度
    test_word_list = PreProcess.clear_word_from_vocab(test_sentence, vocab)
    sim_score = dict()
    i = 1  #保存词向量所在句子的序号
    with open(train_path, 'r', encoding=GlobalParament.encoding) as f_train_reader:
        f_train_reader.readline()
        for train_line in f_train_reader:
            train_line = PreProcess.delete_r_n(train_line)
            train_line_list = train_line.split(',')
            if len(train_line_list) == 2:
                # print('训练集合：' + train_line_list[1])
                train_word_list = train_line_list[1].split()
                train_word_list = PreProcess.clear_word_from_vocab(train_word_list, vocab)
                if len(train_word_list) > 0:
                    # n_similarity
                    sim_score[i] = model.wv.n_similarity(test_word_list, train_word_list)
                i += 1
    sim_score = sorted(sim_score.items(), key=lambda d: d[1], reverse=True)
    return sim_score[0][0]


#用于处理文本数据进行对应输出
def Showans(row,Ans):
    tempRow=1
    f_ans = open(Ans, 'r', encoding='gbk')
    lineAns = f_ans.readline()
    while lineAns:
        if tempRow == row:
            return lineAns
        tempRow += 1
        lineAns = f_ans.readline()

def getAns(test):
    # 测试数据预处理
    # trainFlag = True
    #
    # if not trainFlag:
    #     #训练数据分词预处理
    #     Trainsentences = PreProcess.preprocessing_text(GlobalParament.train_set_dir, GlobalParament.train_after_process_text_dir,
    #                                    GlobalParament.stop_word_dir)
    #     # print(Trainsentences[:10])
    #
    #     #训练数据
    #     MyModel.train(Trainsentences,GlobalParament.model_output_path)
    #     # model = word2vec.KeyedVectors.load_word2vec_format(GlobalParament.model_output_path, binary=True)
    #     model = word2vec.Word2Vec.load(GlobalParament.model_output_path)
    #测试数据预处理
    TestSentences = PreProcess.preprocessing_sentence(test, GlobalParament.test_after_process_text_dir,
                                           GlobalParament.stop_word_dir)
    # print(TestSentences[:10])
    #计算相似度
    ans = calc_sim(GlobalParament.model_output_path, GlobalParament.train_after_process_text_dir,
             TestSentences)

    ansSentennce = Showans(ans,GlobalParament.ans_path)
    return ansSentennce

    #处理文本数据，训练测试用
    # calc_sim(GlobalParament.model_output_path, GlobalParament.train_after_process_text_dir,
    #          GlobalParament.test_after_process_text_dir, GlobalParament.result_out_path)
    # row = 1
    # f = open(GlobalParament.test_set_dir,'r', encoding=GlobalParament.encoding)
    # line = f.readline()
    # while line:
    #     print(line)
    #     Showans(row,GlobalParament.result_out_path,GlobalParament.ans_path)
    #     row +=1
    #     line = f.readline()