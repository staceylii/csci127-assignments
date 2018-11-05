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
        if i == val:
            f = f + 1
    return f

'''
def mode(l):
    msf_value = l[0]
    msf_freq = freq(l, l[0])
    msf_index = 0
    for i in range(len(l)):
        test_freq = freq(l, l[i])
        if test_freq > msf_freq:
            msf_value = l[i]
            msf_index = i
            msf_freq = test_freq
            print("Found new possible mode:")
            print("old mode: ", msf_value, "old freq", msf_freq, "old location: ", msf_index)
            print("new mode: ", 
    return msf_value

a=[]
    for i in l:
        if freq(l, l[i]) >= freq(l,l[li]):
            li=i
    a.append(l[li])
    return a
'''

for i in range (1,5):
    l = build_random_list(10**i, 100)
    start_time = int(round(time.time() * 1000))
    m = mode(l)
    running_time = int(round(time.time() * 1000)) - start time
    print("
        
print(max(list))
print (freq(list, 6))
print(freq([1,2,2,2,2,3,4,5], 1))
print(mode([1,2,2,2,3,4,5]))
print(mode([1,1,1,1,2,4]))