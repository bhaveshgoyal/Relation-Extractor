import os
import nltk
from nltk import *
from stanford_corenlp_pywrapper import CoreNLP

parser = CoreNLP("parse", corenlp_jars=[os.getcwd() + "/stanford-corenlp-full-2015-04-20/*"])
# ner_extracter = CoreNLP("ner", corenlp_jars=[os.getcwd() + "/stanford-corenlp-full-2015-04-20/*"])

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
    parse_res = parser.parse_doc(data)
    # print parse_res
    deptree_list = []
    for each in parse_res["sentences"]:
        deptree_list.append(each['parse'])
    return deptree_list

def ner_extract(data):
    parse_res = ner_extracter.parse_doc(data)
    print parse_res
    # ner_list = []
    # for each in parse_res:
        # ner_list.append(each['ner'])
    # return ner_list

