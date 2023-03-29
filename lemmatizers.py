import parsivar
import hazm

# Creating handle for lemmatize objects
parsivarlemmatize = parsivar.FindStems()
hazmlemmatizer = hazm.Lemmatizer()


def Parsivar_lemma(text):
    return parsivarlemmatize.convert_to_stem(text)

def Hazm_lemma(text):
    return hazmlemmatizer.lemmatize(text)
