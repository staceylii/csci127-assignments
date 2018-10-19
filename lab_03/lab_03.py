import random

adj = ["beautiful", "aggressive", "calm", "delightful", "silly"]
noun = ["tiger", "cat", "house", "banana", "music"]
verb = ["running", "jumping", "swimming", "laughing", "skating"]
plural_noun = ["tigers", "cats", "houses", "bananas", "musics"]
game = ["Scrabble", "Twister", "Tag", "Digging"]
statement = "A vacation is when you take a trip to some <adj> place with your <adj> family. Usually you go to some place that is near a/an <noun> or up on a/an <noun>. A good vacation place is one where you can ride <pnoun> or play <game> or go hunting for <pnoun>. I like to spend my time <verb> or <verb>. When parents go on a vacation, they spend their time eating three <pnoun> a day, and fathers play golf and mothers <verb>."


def madlibs(statement):
    i=0
    space=" "
    newlist = statement.split()
    while i < len(newlist):
        if "<" in newlist[i]:
            if "noun" in newlist[i]:
                index = random.randint(0, len(noun)-1)
                newlist[i] = noun[index]
            if "adj" in newlist[i]:
                index = random.randint(0, len(adj)-1)
                newlist[i] = adj[index]
            if "verb" in newlist[i]:
                index = random.randint(0, len(verb)-1)
                newlist[i] = verb[index]
            if "pnoun" in newlist[i]:
                index = random.randint(0, len(plural_noun)-1)
                newlist[i] = plural_noun[index]
            if "game" in newlist[i]:
                index = random.randint(0, len(plural_noun)-1)
                newlist[i] = game[index] 
        i+=1
    return space.join(newlist)
    
print (madlibs(statement))