import os, json
import jieba
from collections import defaultdict
import jieba.analyse as analyse


def abstract_word(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        trains = json.load(f)
    for index, data in enumerate(trains):
        for id, utt in enumerate(data):
            text = utt['asr_1best']
            manu = utt['manual_transcript']
            if len(utt['semantic']) == 0:
                cut_text = jieba_cut(text)
                cut_manu = jieba_cut(manu)
                cut = list(set(cut_text).intersection(set(cut_manu)))
                if len(cut)/len(cut_manu) >= 0.5:
                    with open('ref.txt', 'a', encoding='utf-8') as fout:
                        fout.write(text+' ')
                        for i in cut:
                            fout.write(i+' ')
                        fout.write('\n')


def jieba_cut(text):
    tf_res = analyse.extract_tags(text, topK=5)
    return tf_res


abstract_word('train.json')