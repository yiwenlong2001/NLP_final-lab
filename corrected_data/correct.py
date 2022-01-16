#coding=utf8
import os, json
import jieba
from collections import defaultdict
from pycorrector.macbert.macbert_corrector import MacBertCorrector
import pycorrector

def correct(filepath):
    with open(filepath+'.json', 'r', encoding='utf-8') as f:
        trains = json.load(f)
    wrong = 0
    m = MacBertCorrector()
    for index, data in enumerate(trains):
        for id, utt in enumerate(data):
            text = utt['asr_1best']
            # MacBERT corrector
            correct_sent, err = m.macbert_correct(text)
            # MacBERT corrector
            # corr_text = pycorrector.correct(text)
            if len(err) > 0:
                wrong += 1
            text = correct_sent
            trains[index][id]['asr_1best'] = text
    with open(filepath+'_new.json', "w", encoding='utf-8') as f:
        json.dump(trains, f, ensure_ascii=False, indent=4)
    return wrong


statistics('train.json')


def cnt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        trains = json.load(f)
    slot_freq = defaultdict(int)
    for data in trains:
        for utt in data:
            sems = utt['semantic']
            for sem in sems:
                slot_freq[sem[1]] += 1
    for k, v in slot_freq.items():
        print(k, v, sep=' ')
        print('\n')

cnt('train.json')

# error_sentence_1 = '我的喉咙发炎了要买点阿莫细林吃'
# correct_sent = pycorrector.correct(error_sentence_1)
# print(correct_sent[0])