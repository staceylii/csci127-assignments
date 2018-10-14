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

print (filterodd([1 ,4, 5, 3, 8, 19]))
print (mapsquare([1 ,4, 5, 3, 8, 19]))