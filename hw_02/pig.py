"""
Stacey Li
Jade Baptiste
"""


def part_pig_latin(name):
    vowels = ('a', 'e', 'i', 'o', 'u',)
    x = name[0]
    if x.startswith(vowels):
            return name + "ay"
    else:
            return name[1:] + x + "ay"

    
print (part_pig_latin ("horace"))