# feature engineer the text 
def textTransform(doc):
    doc = eval(doc)
    output = []
    if (len(doc) == 0):
        return output
    else:
        for each in doc:
            each = re.sub('[0-9]+','',each)
            output.append(each)        
        return output  