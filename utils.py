import os
import nltk
from nltk import *
from stanford_corenlp_pywrapper import CoreNLP

def sen_segment(data):
    """Returns a List of Sentences segmented from test data"""

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(data)
        
def word_tokenize(data):
    """Returns a list of tokens from a given set of data"""

    return nltk.word_tokenize(data)

def dep_parse(data):
    """Creates dependency parser sentence by sentence for given data
    sequence."""

    proc = CoreNLP("parse", corenlp_jars=[os.getcwd() + "/stanford-corenlp-full-2015-04-20/*"])
    parse_res = proc.parse_doc(data)
    deptree_list = []
    for each in parse_res:
        deptree_list.append(each['parse'])
    return deptree_list

def ner_extract(data):
    
    proc = CoreNLP("ner", corenlp_jars=[os.getcwd() + "/stanford-corenlp-full-2015-04-20/*"])
    parse_res = proc.parse_doc(data)
    ner_list = []
    for each in parse_res:
        ner_list.append(each['ner'])
    return ner_list

def filter_ner(ner_list, token_list):

    token_dic = {}
    for each_ner in ner_list:
        if (each_ner == u'O'):



def extract_feature(data):
    """Created tuples and add features to the corr
    list element."""

    for each in ner_extract(data):


