import os
import shutil
import preprocess
from whoosh import qparser , index
from stopwords import stopwords
from time import sleep
from whoosh.filedb.filestore import FileStorage


def search(search_query,SE):
    ix = index.open_dir(SE)
    schema = ix.schema    
    og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(['content'], schema, group = og)
    if SE=="SE0":
        tokenized_list = preprocess.SE0(search_query)
    elif SE=="SE1":
        tokenized_list = preprocess.SE1(search_query)
    elif SE=="SE1_prime":
        tokenized_list = preprocess.SE1_2(search_query)
    elif SE=="SE2":
        tokenized_list = preprocess.SE2(search_query)
    elif SE=="SE2_prime":
        tokenized_list = preprocess.SE2_2(search_query)
    elif SE=="SE3":
        tokenized_list = preprocess.SE3(search_query)
    elif SE=="SE3_prime":
        tokenized_list = preprocess.SE3_2(search_query)
    elif SE=="SE4":
        tokenized_list = preprocess.SE4(search_query)
    elif SE=="SE4_prime":
        tokenized_list = preprocess.SE4_2(search_query)
    parsedQuery = ' '.join(tokenized_list)
    q = mp.parse(parsedQuery)    
    with ix.searcher() as s:
        results = s.search(q, terms=True, limit = 19)
        resultNames = [] 
        for result in results[:]:       
            resultNames.append(result.items()[0][1])
        return resultNames
        
# results_dict = search("زان سوی او چندان وفا زین سوی تو چندین جفا",'SE4_prime')
# print(results_dict)