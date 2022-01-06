import GlobalParament
import PreProcess
from gensim.models import word2vec


def train(sentences, model_out_put_path):
    print('开始训练')
    model = word2vec.Word2Vec(sentences=sentences, vector_size=GlobalParament.train_size, window=GlobalParament.train_window,
                              min_count=1)
    # model.wv.save_word2vec_format(modelBin_out_put_path,binary=True)  #把词向量保存为二进制形式
    # model.wv.save_word2vec_format(modelTxt_out_put_path,binary=True)  #把词向量保存为txt形式
    model.save(model_out_put_path)
    print('训练完成')


if __name__ == "__main__":
    sentences = PreProcess.preprocessing_text(GlobalParament.train_set_dir,GlobalParament.train_after_process_text_dir,GlobalParament.stop_word_dir)
    # print(sentences[:10])
    train(sentences,GlobalParament.model_output_path)

    # model = word2vec.KeyedVectors.load_word2vec_format(GlobalParament.model_output_path, binary=True)
    model = word2vec.Word2Vec.load(GlobalParament.model_output_path)
    # for e in model.wv.most_similar_cosmul(positive=['where']):
    #     print(e[0], e[1])
    # print(len(model.wv))