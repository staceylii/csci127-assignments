def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result

filename="/Users/staceyli/csci127-assignments/moby.txt"
f = open(filename, encoding='utf-8')
s = f.read()
#words_uncleaned = build_word_counts(s)
#print(words_uncleaned)
#print("-------------------")
cleaned_string = clean_data(s)
words = build_word_counts(cleaned_string)
vals = words.values()
vals = sorted(vals)
#print (vals)

def list_comp(l):
    d = {}
    list = l.split()
    for word in list:
        if word not in d.keys():
            d.setdefault(word,[])
    for i in range(0,len(list)-1):
        if list[i] in d.keys():
            d[list[i]].append(list[i+1])
    return d

print(s)
print(list_comp(s))