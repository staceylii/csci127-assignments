1

def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    return name.upper()
print (capitalize("stacey li"))
2

def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    first = name[:1]
    split = breakdown.index(' ')
    after = breakdown[split+1:]

    return first + after
print (init("Stacey Li"))


3

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    x = name[1:]
    return x + name[0] + "ay"
print (part_pig_latin ("Stacey"))
    
"""
4

makeoutword as specified on codingbat.com at
https://codingbat.com/prob/p129981

"""

def make_out_word(out, word):
 return out[0]+out[1]+word+out[2]+out[3]
print (make_out_word("hello", "what"))

5
"""
maketags as specified on codingbat.com at
https://codingbat.com/prob/p132290
"""
def make_tags(tag, word):
    return "<"+tag+">"+word+"</"+tag+">"
print (make_tags("hello", "hi"))
