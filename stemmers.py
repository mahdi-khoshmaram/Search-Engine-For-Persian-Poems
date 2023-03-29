import hazm

# Creating handle for Stemmer object
stemmer = hazm.Stemmer()

def Hazm(text):
    return stemmer.stem(text)