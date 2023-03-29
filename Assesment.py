def assesment():
    fname= "./RelevanceAssesment/RelevanceAssesment"

    relevantfile = list()

    # Reads ReleventAssesment file
    ra = open(fname, encoding="utf8")

    labeled = ra.read().split('\n\n')
    for label in labeled[:-1]:
        labellist = label.split('\n')
        QueryFile = open('./Queries/' + labellist[0], encoding="utf8")
        Query = QueryFile.read()
        resultList = labellist[1].split(' ')
        relevantfile.append((Query,resultList))
    return relevantfile


