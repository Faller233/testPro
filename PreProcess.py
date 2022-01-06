#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 停用词+分词+数据预处理

import GlobalParament
import jieba


# 去掉回车行
def delete_r_n(line):
    return line.replace('\r', '').replace('\n', '').strip()


# 读取停用词
def get_stop_words(stop_words_dir):
    stop_words = []
    with open(stop_words_dir, 'r', encoding=GlobalParament.encoding) as f_reader:
        for line in f_reader:
            line = delete_r_n(line)
            stop_words.append(line)
    stop_words = set(stop_words)
    return stop_words


# jieba精准分词
def jieba_cut(content, stop_words):
    word_list = []
    if content != '' and content is not None:
        seg_list = jieba.cut(content)
        for word in seg_list:
            if word not in stop_words:
                word_list.append(word)
    return word_list


# 结巴搜索引擎分词
def jieba_cut_for_search(content, stop_words):
    word_list = []
    if content != '' and content is not None:
        seg_list = jieba.cut_for_search(content)
        for word in seg_list:
            if word not in stop_words:
                word_list.append(word)
    return word_list


# 清理不在词汇表中的词语
def clear_word_from_vocab(word_list, vocab):
    new_word_list = []
    for word in word_list:
        if word in vocab:
            new_word_list.append(word)
    return new_word_list


# 文本预处理第一种方法Pandas
def preprocessing_sentence(text_sec, after_process_text_dir, stop_word_dir):
    stop_words = get_stop_words(stop_word_dir)
    word_list = jieba_cut(text_sec, stop_words)
    # print(word_list)
    # print(np.array(word_list).shape)
    return word_list


# 文本预处理第二种方法
def preprocessing_text(text_dir, after_process_text_dir, stop_word_dir):
    stop_words = get_stop_words(stop_word_dir)
    sentences = []
    f_writer = open(after_process_text_dir, 'w', encoding=GlobalParament.encoding)
    # count = 0
    with open(text_dir, 'r', encoding=GlobalParament.encoding) as f_reader: #txt编码方式为gbk
        for line in f_reader:
            line_list = line.split(",")
            if len(line_list) > 0:
                line_list2 = delete_r_n(line_list[0])#
                word_list = jieba_cut(line_list2, stop_words)
                sentences.append(word_list)
                f_writer.write(line_list[0] + "," + " ".join(word_list) + '\n') #csv
                # f_writer.write(line_list[0]  + " ".join(word_list) + '\n') #txt
                f_writer.flush()
                # count =count + 1
                # print(count)
    f_writer.close()
    return sentences


# if __name__ == "__main__":
#处理单个句子
    # test = '你好'
    # TestSentences = preprocessing_sentence(test,GlobalParament.test_after_process_text_dir,GlobalParament.stop_word_dir)
    # print(TestSentences[:5])
#处理txt文件
#     # stop_words = get_stop_words(GlobalParament.stop_word_dir)
#     Trainsentences = preprocessing_text(GlobalParament.train_set_dir, GlobalParament.train_after_process_text_dir,
#                                    GlobalParament.stop_word_dir)
#     print(Trainsentences[:10])
#
#     Testsentences = preprocessing_text(GlobalParament.test_set_dir, GlobalParament.test_after_process_text_dir,
#                                    GlobalParament.stop_word_dir)
#     print(Testsentences[:10])