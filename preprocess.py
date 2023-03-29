from normalizers import parsivar_normalizer, Hazm_normalizer
from lemmatizers import Parsivar_lemma, Hazm_lemma
import stemmers
from whoosh.analysis import StandardAnalyzer
from stopwords import stopwords

# Lists stopwords from reading stopwords folder
stopwords = stopwords()

# Creating analyzer handles
ana = StandardAnalyzer()
stop_ana = StandardAnalyzer(stoplist=frozenset(stopwords))




def SE0(input) :
    tokenized_list = [token.text for token in ana(input)]
    return tokenized_list

def SE1(input) :
    string = Hazm_normalizer(input)
    tokenized_list = [token.text for token in ana(string)]
    return tokenized_list

def SE1_2(input) :
    string = parsivar_normalizer(input)
    tokenized_list = [token.text for token in ana(string)]
    return tokenized_list

def SE2(input) :
    string = Hazm_normalizer(input)
    tokenized_list = [token.text for token in stop_ana(string)]
    return tokenized_list

def SE2_2(input) :
    string = parsivar_normalizer(input)
    tokenized_list = [token.text for token in stop_ana(string)]
    return tokenized_list

def SE3(input) :
    string = Hazm_normalizer(input)
    tokenized_list = [Hazm_lemma(token.text) for token in stop_ana(string)]
    return tokenized_list

def SE3_2(input) :
    string = parsivar_normalizer(input)
    tokenized_list = [Parsivar_lemma(token.text) for token in stop_ana(string)]
    return tokenized_list

def SE4(input) :
    string = Hazm_normalizer(input)
    tokenized_list = [stemmers.Hazm(token.text) for token in stop_ana(string)]
    return tokenized_list

def SE4_2(input) :
    string = Hazm_normalizer(input)
    tokenized_list = [stemmers.Hazm(token.text) for token in stop_ana(string)]
    return tokenized_list