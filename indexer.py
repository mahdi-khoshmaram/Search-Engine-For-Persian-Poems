import os
import shutil
import preprocess
from stopwords import stopwords
from time import sleep
from whoosh import index
from whoosh.fields import Schema, TEXT, STORED
from whoosh.filedb.filestore import FileStorage


def index(dirname):
    # Creating schema
    schema = Schema(content=TEXT, docID=TEXT(stored=True))

    # Deletes previous index directories
    try:
        shutil.rmtree(dirname)
        print('Removing previous index directory\nPlease wait...\n')
        sleep(2)
        os.system('cls')
    except:
        pass
    
    # Creates index directory
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    
    # Creates index object
    storage = FileStorage(dirname)
    ix = storage.create_index(schema)
    ix = storage.open_index()

    #Gets poems file names from Poems folder
    poems_list = os.listdir('./Poems')

    # Starts indexing
    writer = ix.writer()
    print('Indexing started...')
    i = 0
    for doc in poems_list:
        with open('./Poems/'+doc, encoding="utf8") as fh:
            if dirname=="SE0":
                tokenized_list = preprocess.SE0(fh.read())
            elif dirname=="SE1":
                tokenized_list = preprocess.SE1(fh.read())
            elif dirname=="SE1_prime":
                tokenized_list = preprocess.SE1_2(fh.read())
            elif dirname=="SE2":
                tokenized_list = preprocess.SE2(fh.read())
            elif dirname=="SE2_prime":
                tokenized_list = preprocess.SE2_2(fh.read())
            elif dirname=="SE3":
                tokenized_list = preprocess.SE3(fh.read())
            elif dirname=="SE3_prime":
                tokenized_list = preprocess.SE3_2(fh.read())
            elif dirname=="SE4":
                tokenized_list = preprocess.SE4(fh.read())
            elif dirname=="SE4_prime":
                tokenized_list = preprocess.SE4_2(fh.read())
            os.system('cls')
            writer.add_document(content=tokenized_list, docID=doc)
            i = i + 1
            print(f"Indexing...\n{round((int(i)/(len(poems_list)))*100)}%")
    os.system('cls')
    writer.commit()
    print('\Indexing completed/')

