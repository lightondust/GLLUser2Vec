from gensim import matutils
import numpy as np
from server.config import NODE2VEC_MODEL_PATH, RESULT_NODES_NO
from gensim.models import Word2Vec
import json


def load_user_data(data_path):
    with open(data_path, 'r') as f:
        user_dict = json.load(f)
    return user_dict


def load_model(model_path=NODE2VEC_MODEL_PATH):
    model_load = Word2Vec.load(model_path)
    return model_load


def get_nodes_link_from(model, node, topn):
    return model.predict_output_word([node], topn=topn)


def get_nodes_link_to(model, node, topn):
    """
    re-use implementation of gensim

    :param model: gensim.models.Word2Vec
    :param node:
    :param topn:
    :return:
    """

    word_vocabs = [model.wv.vocab[node]]
    word2_indices = [word.index for word in word_vocabs]

    l1 = np.sum(model.trainables.syn1neg[word2_indices], axis=0)
    if word2_indices and model.cbow_mean:
        l1 /= len(word2_indices)

    prob_values = np.exp(np.dot(l1, model.wv.vectors.T))
    prob_values /= sum(prob_values)
    top_indices = matutils.argsort(prob_values, topn=topn, reverse=True)
    return [(model.wv.index2word[index1], prob_values[index1]) for index1 in top_indices]


def get_likely_be_mentioned(model, node, topn=RESULT_NODES_NO):
    return get_nodes_link_from(model, node, topn=topn)


def get_likely_mention(model, node, topn=RESULT_NODES_NO):
    return get_nodes_link_to(model, node, topn=topn)


def get_similar_node(model, node, topn=RESULT_NODES_NO):
    return model.similar_by_word(node, topn=topn)