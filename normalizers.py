import parsivar
import hazm

# Creating handle for normalizer objects
parsivarnorm = parsivar.Normalizer()
hazmnorm = hazm.Normalizer()


def parsivar_normalizer(text):
    return parsivarnorm.normalize(text)


def Hazm_normalizer(text):
    return hazmnorm.normalize(text)