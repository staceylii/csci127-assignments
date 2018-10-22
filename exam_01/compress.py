def compress_word(w):
    new = []
    vowel = 'a','e','i','o','u'
    for item in w:
        if item not in vowel:
            new.append(item)
    result = ''.join(new)
    return result

print (compress_word('halloween'))
print (compress_word('special'))
print (compress_word('apple'))
print (compress_word('amazing'))

def sentence(line):
    listword = []
    newsent = line.split()
    for item in newsent:
        listword.append(compress_word(item)+' ')
    combined = ''.join(listword)
    return combined
print (sentence('i like to eat apple pie.'))
print (sentence('who is there'))
print (sentence('i am pushing to github'))