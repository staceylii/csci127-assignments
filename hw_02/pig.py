"""
Stacey Li
Jade Baptiste
""""


def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    vowel = 'aeiou'
    if name[0] not in vowel:
        x = name[1:]
        return x + name[0] + "ay"
    else:
        return name
    
print (part_pig_latin ("horace"))