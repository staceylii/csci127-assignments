#not sure why half the code is running

import random

dict = {}
dict['adj'] = ['beautiful', 'aggressive', 'calm', 'delightful', 'silly']
dict['noun'] = ['tiger', 'cat', 'house', 'banana', 'music']
dict['verb'] = ['running', 'jumping', 'swimming', 'laughing', 'skating']
dict['plural_noun'] = ['tigers', 'cats', 'houses', 'bananas', 'musics']
dict['game'] = ['Scrabble', 'Twister', 'Tag', 'Digging']

statement = "A vacation is when you take a trip to some <adj> place with your <adj> family. Usually you go to some place that is near a/an <noun> or up on a/an <noun>. A good vacation place is one where you can ride <pnoun> or play <game> or go hunting for <pnoun>. I like to spend my time <verb> or <verb>. When parents go on a vacation, they spend their time eating three <pnoun> a day, and fathers play golf and mothers <verb>."

def madlibs(statement, word):
    newlist = statement.split()
    newsentence = []
    for item in newlist:
        if item == '<adj>':
            newsentence.append((dict['adj'][random.randrange(len(dict['adj']))]))
        elif item  == '<noun>':
            newsentence.append((dict['noun'][random.randrange(len(dict['noun']))]))
        elif item == '<verb>':
            newsentence.append((dict['verb'][random.randrange(len(dict['verb']))]))
        elif item == '<pnoun>':
            newsentence.append((dict['plural_noun'][random.randrange(len(dict['plural_noun']))]))
        elif item == '<game>':
            newsentence.append((dict['game'][random.randrange(len(dict['game']))]))
        else:
            newsentence.append(item)
    return ' '.join(newsentence)

print (madlibs(statement, dict))
