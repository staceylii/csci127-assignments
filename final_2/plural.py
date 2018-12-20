def countPlurals(line):
    for i in line:
        count = 0
        new = line.split()
        for word in new:
            if word[-1] == 's':
                count += 1
    return count

def notPossessive(line):
    for i in line:
        count2 = 0
        new = line.split()
        for word in new:
            if word[-2] != "'" and word[-1] == 's':
                count2 += 1
    return count2

print (countPlurals("There are horses and cows and bears"))
print (countPlurals("shoes shoe hoof hooves letters"))
print (notPossessive("There are horse's and cow's"))
print (notPossessive("sheriff's sherrifs"))