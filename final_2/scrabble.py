def canMakeWord(letters,word):
    wordlist = list(letters)
    for i in word:
        if i in wordlist:
            wordlist.remove(i)
        else:
            return False
    return True

print(canMakeWord("ladilmy", "daily"))
print(canMakeWord("eerriin", "eerie"))
print(canMakeWord("orrpgma", "program"))
print(canMakeWord("orppgma", "program"))


def withWild(letters, word):
    wordlist = list(letters)
    for i in word:
        if i in wordlist:
            wordlist.remove(i)
        elif "?" in wordlist:
            wordlist.remove("?")
        else:
            return False
    return True


print(withWild("dai??ly", "daily"))
print(withWild("??gam", "program"))
print(withWild("??program", "program"))