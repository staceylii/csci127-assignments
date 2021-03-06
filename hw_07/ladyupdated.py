"""
def adjacentbug(b): 
    #checks to see if its next to each other
    adjacent = False 
    for i in range(len(b)):
        if i == 0:
           if b[i] == b[i+1]:
               adjacent = True
           else:
                adjacent = False
                break
        elif i == (len(b)-1):
            if b[i-1] == b[i]:
                adjacent = True
            else:
                adjacent = False
                break
        elif b[i] == b[i+1] or b[i] == b[i-1]:
          adjacent = True

    return adjacent


def underscore(b):
    for i in b:
        if i == "_":
            return True
    return False

def happy(b):
    happybug = False
    for i in b:
        if i != "_":
            count = 0
            for c in b:
                if i == c:
                    count += 1
            if count >= 2:
                happybug = True
            else:
                happybug = False
                break
        return happybug
        
def happyLadybug(b):
    if b == "":
        return "There's no input."
    if b == "_":
        return "The ladybugs are happy."
    if adjacentbug(b):
        return "The ladybugs are happy."
    elif underscore(b):
        if happy(b):
            return "The ladybugs are happy."
        else:
            return "The ladybugs are not happy."
    return "The ladybugs are not happy."
    
        
print(adjacentbug("AABBCC"))
print(underscore("AABB_C"))
print(happy("AABBCC"))
print(happyLadybug("AABB_C"))
print(happyLadybug("ABCDEF"))
print(happyLadybug("JKLAAC"))
print(happyLadybug("AABB"))
print(happyLadybug("AABB_CC"))
print(happyLadybug("___"))
print(happyLadybug("_"))
print(happyLadybug(""))
print(happyLadybug("ABAB_"))
"""


def underscore(b):
    for i in b:
        if i == '_':
            return True
        else:
            return False
    return underscore(b)


def adjacentbug(b): 
    #checks to see if its next to each other
    adjacent = False 
    for i in range(len(b)):
        if i == 0:
           if b[i] == b[i+1]:
               adjacent = True
           else:
                adjacent = False
                break
        elif i == (len(b)-1):
            if b[i-1] == b[i]:
                adjacent = True
            else:
                adjacent = False
                break
        elif b[i] == b[i+1] or b[i] == b[i-1]:
          adjacent = True

    return adjacent


def letters(b):
    letters = False
    dict = {}
    for i in b:
        if i != "_":
            dict[i]=0
            for c in b:
                if i == c:
                    dict[i]+=1
            if dict[i] >= 2 and "_" in b:
                letters = True
            else:
                letters = False
                break
    return letters

def happy(b):
    if adjacentbug(b):
        return "YES"
    elif letters(b):
        return "YES"
    elif underscore(b):
        return "NO"
    else:
        return "NO"

print (underscore("AAB_C"))
print (adjacentbug("AAB_C"))
print (letters("AAB_C"))
print (letters("AABC"))
print (letters("AABBDD_"))
print (happy("AAB_C"))
