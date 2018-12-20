def addline(d, line):
    lower = line.lower()
    for i in lower.split():
        if i[0] in d:
            d[i[0]].append(i)
        else:
            d[i[0]] = [i]
    return d
            


def spellcheck (d,word):
    lower = word.lower()
    if word in d[lower[0]]:
        return True
    else:
        return False
        

dict = {}

print(addline(dict, "when in the course of human events"))
print(addline(dict, "a scrub is a guy who thinks"))
print(addline(dict, "i want it that way"))
print(addline(dict, "jealousy turning saints into the sea swimming through sick lullabies"))
print(addline(dict, "Choking on your alibis but its just the price I pay"))
print(addline(dict, "DeStInY is CAlLiNg mE open up your eager eyEs"))


print(spellcheck(dict, 'human'))
print(spellcheck(dict, 'scrubs'))
print(spellcheck(dict, 'way'))
print(spellcheck(dict, 'truning'))
print(spellcheck(dict, 'alibis'))