# coding: utf8
import csv
import string
import nltk

traindata = 'data.txt'
inputdata = 'input.txt'
matrix = dict()
V = 0


def train(data):
    # {Wi:[c1,c2,c3]}
    for row in data:
        for word in row[0]:
            if word not in matrix:
                matrix.update({word: [row[1]]})
            else:
                if row[1] in matrix[word]:
                    pass
                else:
                    matrix[word].append(row[1])
    V = len(matrix)
#    for key in matrix.keys():
#        print key, matrix[key]



def classify(data):
    # [[w1,w2,w3]]
    translate_table = dict((ord(char), None) for char in string.punctuation)
    with open(data) as file:
        raw = csv.reader(file) # [sentence, sentence, sentence ...]
        raw = [tmp.decode('utf-8').lower() for tmp in raw]
        raw = [tmp.translate(translate_table) for tmp in raw]
        raw = [nltk.word_tokenize(tmp) for tmp in raw]
        #for tmp in raw:
        #    print tmp



def load(data):
    # [[words],[class]]
    translate_table = dict((ord(char), None) for char in string.punctuation)
    with open(data) as file:
        raw = csv.reader(file, delimiter=';')
        raw = [[tmp[0].decode('utf-8').lower().replace('\n', ''), tmp[1]] for tmp in raw]
        raw = [[tmp[0].translate(translate_table), tmp[1]] for tmp in raw]
        raw = [[nltk.word_tokenize(tmp[0]), tmp[1]] for tmp in raw]
        return raw


data = load('data.csv')
train(data)
classify('input.csv')