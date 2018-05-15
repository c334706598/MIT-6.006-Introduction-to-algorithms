# -*- coding: utf-8 -*-
"""
Created on Tue May 15 23:14:31 2018

@author: XIN
"""
import math

def split_into_words(doc):
    i = 0
    ans = []
    word = ""
    for i in range(len(doc)):
        if (doc[i] >= '0' and doc[i] <= '9') or (doc[i] >= 'a' and doc[i] <= 'z') or (doc[i] >= 'A' and doc[i] <= 'Z'):
            word += doc[i]
        else:
            if word:
                ans.append(word)
            word = ""
        i += 1
    if word:
        ans.append(word)
    return ans

def word_count(words):
    count = {}
    for word in words:
        if word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    return count

def doc_dist(doc1, doc2):
    words1 = split_into_words(doc1)
    words2 = split_into_words(doc2)
    count1 = word_count(words1)
    count2 = word_count(words2)
    res = 0
    norm1 = 0
    for word in count1:
        if word in count2:
            res += count1[word] * count2[word]
        norm1 += count1[word] ** 2
    norm1 = norm1 ** 0.5
    norm2 = 0
    for word in count2:
        norm2 += count2[word] ** 2
    norm2 = norm2 ** 0.5
    return math.acos(res/norm1/norm2)/math.pi*180
    

doc_1 = 'I once had a girl, or should I say she once had me.'
doc_2 = 'I once had a girl, or should I say she once'
#words_1 = split_into_words(doc_1)
#words_2 = split_into_words(doc_2)
#print(words)
#count_1 = word_count(words_1)
#count_2 = word_count(words_2)
#print(count_1)
#print(count_2)
print(doc_dist(doc_1, doc_2))
