"""
def filterodd(l):
    i = 0
    odd = []
    while i < len(l):
        if l[i] % 2 != 0:
            odd.append(l[i])
    return odd
    
def mapsquare(l):
    i = 0
    square = []
    while i < len(l):
        square.append(l[i] * l[i])
    return square
"""


def mapsq_while(l):
    result = []
    i = 0
    while i <len(l):
        result.append(l[i]*l[i])
        i = i + 1
    return result

def filter_odd(l):
    result = []
    for item in l:
        if item % 2 != 0:
            result.append(item)
        return result
    

print (filter_odd([1 ,4, 5, 3, 8, 19]))
print (mapsq_while([1 ,4, 5, 3, 8, 19]))