#Sam Ebersole
#Stacey Li

import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l

def locate(l, value):
    search = 0
    found = False
    while found == False:
        if search >= len(l):
                search = -1
                found = True
        else:
            if l[search] == value:
                found = True
            else:
               search += 1
    return search

def count(l, value):
    search = 0
    count = 0
    while search < len(l):
        if l[search] == value:
            count += 1
            search += 1
        else:
            search += 1
    return count

def reverse(l):
    search = len(l) - 1
    lnew = []
    while search != -1:
        lnew.append(l[search])
        search -= 1
    return lnew

def isIncreasing(l):
    search = 1
    oldCheck = 0
    increasing = True
    while len(l) > search:
        if l[search] > l[oldCheck]:
            search += 1
            oldCheck += 1
        else:
            increasing = False
            search += 1
            oldCheck += 1
    return increasing

def palindrome(l):
    leftCheck = 0
    rightCheck = len(l) - 1
    isPalindrome = True
    while leftCheck <= rightCheck:
        if l[leftCheck] == l[rightCheck]:
            leftCheck += 1
            rightCheck -= 1
        else:
            isPalindrome = False
            leftCheck += 1
            rightCheck -= 1
    return isPalindrome

l = build_random_list(5, 5)
value = random.randrange(0,5)
print(l)
print(value)
print(locate(l, value))
print(count(l, value))
print(reverse(l))
print(isIncreasing(l))
print(palindrome(l))