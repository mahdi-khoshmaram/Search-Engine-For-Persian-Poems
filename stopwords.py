import os
def stopwords():
    stopwords = list()
    filehandle = open('./stopwords/Stopwords',encoding='utf8') 
    for i in filehandle:
        stopwords.append(i.strip())

    return stopwords