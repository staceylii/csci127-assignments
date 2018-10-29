import random
list = []
for i in range(100):
    list.append(random.randrange(1,11))
print(list)

def max(l):
    p = []
    li = 0
    for i in range(1, len(list)):
        if list[i] > list[li]:
            li = i
    return li

def freq(l,val):
    f = 0
    for i in l:
        if l[i] == val:
            f = f + 1
    return f


def mode(l):
    li=0
    a=[]
    for i in l:
        if freq(l, l[i]) >= freq(l,l[li]):
            li=i
    a.append(l[li])
    return a
    
print(max(list))
print (freq(list, 6))
print(freq([1,2,2,2,2,3,4,5], 1))
print(mode([1,2,2,2,3,4,5]))
print(mode([1,1,1,1,2,4]))