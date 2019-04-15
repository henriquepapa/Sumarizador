# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:39:50 2019

@author: henri
"""

def def_sujeito_grande (sentence, root):
    sujeito = ""
    sentence = nltk.word_tokenize(sentence)
    for token in sentence:
        if(token!=root):
            sujeito = sujeito + " " + token
        else:
            break
    return sujeito

def def_sujeito(sentence,root,nsubj) :
    sujeito = ""
    yes = 0
    sentence = nltk.word_tokenize(sentence)
    for token in sentence:
        if token == nsubj:
            yes = 1
        if(token!=root and yes == 1):
            sujeito = sujeito + " " + token
        elif(token == root):
            break
    return sujeito
    

import spacy
import nltk
pln= spacy.load('pt')
doc = ('A aviação de Israel realizou durante a madrugada desta segunda-feira, dia 7, ataques a 150 alvos no Líbano. Enquanto isso, soldados israelenses mataram 10 integrantes da milícia do Hezbollah. Durante este domingo, dia 6, foram travadas lutas sangrentas. Os foguetes e ataques do Hezbollah causaram a morte de 15 pessoas e deixaram mais de 200 feridas. Já o Exército de Israel provocaram a morte de 30 militantes do Hezbollah. Comandos israelenses mataram outros três guerrilheiros libaneses na cidade de Tiro, onde destruíram sete plataformas de lançamento de foguetes, informaram as fontes israelenses.')
doc = nltk.sent_tokenize(doc)
for sentence in doc:
    sujeito = ""
    texto = pln(sentence)
    root = [token for token in texto if token.head == token][0]
    for token in texto:
        if token.dep_ == 'nsubj':
            sujeito = token.text
            #print(sujeito)
            sujeito = def_sujeito(sentence,str(root),str(sujeito))
        if str(token.text) == str(root):
            break
    if sujeito == "":
        sujeito = def_sujeito_grande(sentence,str(root))
    print(sujeito)
