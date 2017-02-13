# coding: utf8
import csv
import string
import nltk

traindata = 'data.txt'
inputdata = 'input.txt'
matrix = dict()
instances = list()  # number of instances per class
V = 0  # vocabulary
c = 0  # number of classes
N = 0  # number of classes instances


def train(data):
    # {Wi:[N1,N2,N3]} -> ci -- count of word in class ci
    global c, V, N, instances
    for row in data:
        N += 1
        if c < int(row[1]): c = int(row[1])
    instances = [0]*c
    for row in data:
        instances[int(row[1])-1] += 1
        for word in row[0]:
            if word not in matrix:
                matrix.update({word: [0]*c})
                matrix[word][int(row[1])-1] += 1
            else:
                matrix[word][int(row[1])-1] += 1
    V = len(matrix)
#    for key in matrix.keys():
#        print key, matrix[key]


def classify(data):
    # [[w1,w2,w3], [w4,w5,w6]]
    global matrix, instances, N, V, c
    translate_table = dict((ord(char), None) for char in string.punctuation)
    with open(data) as file:
        raw = csv.reader(file, delimiter =';')  # [sentence, sentence, sentence ...]
        raw = [tmp[0].decode('utf-8').lower() for tmp in raw]
        raw = [tmp.translate(translate_table) for tmp in raw]
        raw = [nltk.word_tokenize(tmp) for tmp in raw]
        # FIX
        for row in raw:
            sentence_probability = 0
            for cls in xrange(c):
                unique_words = unique_words_count(cls)
                class_probability = float(instances[cls]/N)
                for word in row:
                    if word in matrix:
                        class_probability *= (matrix[word][cls] + 1)/(unique_words + V)
                    else:
                        class_probability *= 1/(unique_words + V)
                if sentence_probability < class_probability:
                    sentence_probability = class_probability
                    row.append(cls)
                



def unique_words_count(cls):
    count = 0
    for word in matrix:
        if matrix[word][cls] != 0:
            count += 1
    return count


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
