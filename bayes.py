# coding: utf8
from __future__ import division  # integer to floating point division
import string
import nltk

matrix = dict()  # word matrix
sentences = list()  # P(c) - class probability
V = 0  # vocabulary
c = 0  # number of classes
N = 0  # number of sentences


def train(data):
    # {Wi:[N1,N2,N3]} -> ci -- count of word in class ci
    global c, V, N, sentences
    for row in data:
        N += 1
        if c < int(row[1]): c = int(row[1])
        sentences = [0]*c
    for row in data:
        sentences[int(row[1]) - 1] += 1
        for word in row[0]:
            if word not in matrix:
                matrix.update({word: [0]*c})
                matrix[word][int(row[1])-1] += 1
            else:
                matrix[word][int(row[1])-1] += 1
    for i in xrange(c):
        sentences[i] = float(sentences[i]/N)
    V = len(matrix)


def classify(data):
<<<<<<< HEAD
    # [[w1,w2,w3], [class], [classified],
    # [w4,w5,w6], [class], [classified]]
    global matrix, sentences, N, V, c
    for i, row in enumerate(data):
        sentence_probability = 0  # P(wi|cj) - saves heightest sentence probability for class
        type = 0  # sentence class
        for cls in xrange(c):
            unique_words = unique_words_count(cls)  # number of unique words per class
            class_probability = float(sentences[cls])  # P(c)
            for word in row[0]:
                if word in matrix:
                    class_probability *= (matrix[word][cls] + 1)/(unique_words + V)
                else:
                    class_probability *= 1/(unique_words + V)
            if sentence_probability < class_probability:
                sentence_probability = class_probability
                type = cls + 1
        data[i].append(type)
    return data
=======
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
                

>>>>>>> e722dd237e55558cb7f88435acc5e79481d99716


def unique_words_count(cls):
    count = 0
    for word in matrix:
        if matrix[word][cls] != 0:
            count += 1
    return count


def load(data):
    # [[w1,w2,w3,w4],[class],
    # [w1,w2,w3,w4],[class]]
    # ham - 1
    # spam - 2
    translate_table = dict((ord(char), None) for char in string.punctuation)
    with open(data) as file:
        raw = file.readlines()
        raw = [tmp.decode('utf-8').lower().strip() for tmp in raw]
        raw = [tmp.translate(translate_table) for tmp in raw]
        raw = [nltk.word_tokenize(tmp) for tmp in raw]
        raw = [[tmp, 0] for tmp in raw]
        for i, row in enumerate(raw):
            if row[0][0] == 'ham':
                raw[i][1] = 1
            if row[0][0] == 'spam':
                raw[i][1] = 2
            raw[i][0].pop(0)
        return raw


def preciseness(data):
    N = 0
    for row in data:
        if row[1] == row[2]:
            N += 1
    print 'Preciseness: {}%'.format(N*100/len(data))


data = load('SMSSpamCollection.txt')
train(data)
<<<<<<< HEAD
data = load('input.txt')
data = classify(data)
preciseness(data)
=======
classify('input.csv')
>>>>>>> e722dd237e55558cb7f88435acc5e79481d99716
