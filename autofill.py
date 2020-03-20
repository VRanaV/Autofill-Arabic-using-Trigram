import nltk
import numpy as np
import string
import re


from nltk import word_tokenize,sent_tokenize

file= open('C:/Users/User/.spyder-py3/sports.txt',encoding="utf8")
data=file.read()


data=re.sub('[^\s ء-ي]', '',data)
prob={}    
ngrams={}
words=3

wordsTokens=nltk.word_tokenize(data)
count=0
# print(wordsTokens)

for i in range(len(wordsTokens)-words):
    seq=' '.join(wordsTokens[i:i+words])
    if seq not in ngrams.keys():
        ngrams[seq]=1
        count +=1
    else:
        ngrams[seq]+=1
        count+=1
    prob[seq]=ngrams[seq]/count

# print(prob.keys())
def predict(input):
    input_word=input.split(" ")
    output_list=[]
    for i in prob.keys():
        if input in  i :
            if i.split(" ")[0] != input_word[0] or i.split(" ")[1] != input_word[1]:
                continue
            output_list.append((i,prob[i]))

    output_list.sort(key=lambda x: x[1],reverse=True)

    numOfSuggestions = 10
    if numOfSuggestions > len(output_list):
        numOfSuggestions = len(output_list)

    print("    ",input)
    for i in range( 0 , numOfSuggestions ):
        print(output_list[i][0].split(" ")[2])
                
predicted = input('Enter your first 2 words : ')
predict(predicted)
## يحتاج الى
    
