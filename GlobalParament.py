import os

#停用词
stop_word_dir = os.getcwd()+'\data\cn_stopwords.txt'
#编码方式，中文
encoding = 'utf8'
#测试数据
test_set_dir = os.getcwd()+'\data//test.txt'
#测试数据的分词结果
test_after_process_text_dir = os.getcwd()+'\data//tested.csv'

#训练数据
train_set_dir = os.getcwd()+'\data//train.txt'
#训练数据的分词结果
train_after_process_text_dir = os.getcwd()+'\data//trained.csv'

#模型输出路径
model_output_path = os.getcwd()+'\model\\model.npy'
modelBin_output_path = os.getcwd()+'\model\\model.bin'
modelTxt_output_path = os.getcwd()+'\model\\model.txt'

#word2Vec训练模型参数
train_size = 1500
train_window = 5

#结果
result_out_path = os.getcwd() +'\data//ans.txt'
ans_path = os.getcwd() +'\data//ans.csv'