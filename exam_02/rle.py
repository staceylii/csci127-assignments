'''
def encode(b):
    #checks to see if its next to each other
    d = {}
    count = 1
    for i in b:
        if len(i) > 0:
            for c in b:
                if i == c:
                    count += 1
                    d.append(i, count)
            else:
                return count

    return d
print(encode('aabbaacddaaa'))

'''

def encode(b):
    count = 1
    value =[]
    for i in range(len(b)):
        if i == len(b)-1 or b[i] != b[i+1]:
            value.append([b[i], count])
            count = 1
        else:
            count+=1           
    return value
        
print(encode('aabbaaacddaaa'))
print(encode('abcd'))
print(encode('cbbbbdee'))

def decode(input):
    a = ""
    for i in input:
        for b in range(i[1]):
            a+=i[0]
    return a

print(decode([['a', 2], ['b', 2], ['a', 3], ['c', 1], ['d', 2], ['a', 3]]))
print(decode([['c', 1], ['b', 4], ['d', 1], ['e', 2]]))