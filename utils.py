import os
import subprocess
import nltk
from nltk import *
from stanford_corenlp_pywrapper import CoreNLP

parser = CoreNLP("parse", corenlp_jars=[os.getcwd() + "/stanford-corenlp-full-2015-04-20/*"])
ner_extracter = CoreNLP("ner", corenlp_jars=[os.getcwd() + "/stanford-corenlp-full-2015-04-20/*"])

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
    deptree_list = []
    for each in parse_res["sentences"]:
        deptree_list.append(each['parse'])
    return deptree_list

def ner_extract(data):
    parse_res = ner_extracter.parse_doc(data)
    ner_list = []
    for each in parse_res['sentences']:
        ner_list.append(each['ner'])
    return ner_list

def get_chunklink(parsed_data):
    ofp = open("dep_parsed.txt", "w")
    for each in parsed_data:
        ofp.write(each.replace("ROOT", "", 1)+"\n")
    ofp.close()
    out = os.popen('perl chunklink.pl dep_parsed.txt').read()
    chunklinked = out.split('\n')[2:]
    chunklinked = "\n".join(chunklinked)
    chunklinked = chunklinked.split('\n\n')
    del chunklinked[-1]
    for x in xrange(len(chunklinked)):
        line = []
        for each in chunklinked[x].split('\n'):
            line.append(each)
        line2 = []
        for each in line:
            a = []
            e = each.split(' ')
            for k in e:
                if k!='':
                    a.append(k)
            line2.append(a)
        chunklinked[x] = line2
    return chunklinked

def combiner(chunked, ner):
    for x in xrange(len(chunked)):
        for y in xrange(len(chunked[x])):
            chunked[x][y].append(ner[x][y])
    return chunked

def get_data(filename):
    data = open(filename, 'r').read()
    return data


def get_in_format():
    data = get_data('in')
    parsed = dep_parse(data)
    chunked = get_chunklink(parsed)
    ner = ner_extract(data)
    chunked = combiner(chunked, ner)

    entities = []
    for chunk in chunked:
        sen_entities = []
        for stream in chunk:
            if (stream[-1] != u'O'):
                sen_entities.append(stream)
        entities.append(sen_entities)

    return entities
