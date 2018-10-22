def compress_word(w):
    vowel = 'a','e','i','o','u'
    new = []
    for item in w:
        if item not in vowel:
            new.append(item)
    result = ''.join(new)
    return result

print (compress_word('halloween'))
print (compress_word('special'))
print (compress_word('apple'))

def sentence(line):
    listword = []
    newsent = line.split()
    for item in newsent:
        listword.append(compress_word(item)+' ')
    newLine = ''.join(listword)
    return newLine
print (sentence('i like to eat apple pie.'))
print (sentence('who is there'))