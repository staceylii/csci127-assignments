def makeacronym(w):
    words = w.split()
    for i in words:
        letters = [word[0] for word in words]
        return "".join(letters)

print(makeacronym('laugh out loud'))
print(makeacronym('read the fine manual'))
print(makeacronym('in my humble opinion'))
print(makeacronym('in my not so humble opinion'))
print(makeacronym('rolling on floor laughing'))