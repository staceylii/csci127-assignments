def score(w):
    one = "a,e,i,o,u,l,n,r,s,t"
    two = "d,g"
    three = "b,c,m,p"
    four = "f,h,v,w,y"
    five = "k"
    eight = "j,x"
    ten = "q,z"
    score = 0
    
    for i in w:
        if i in one:
            score += 1
        if i in two:
            score += 2
        if i in three:
            score += 3
        if i in four:
            score += 4
        if i in five:
            score += 5
        if i in eight:
            score += 8
        if i in ten:
            score += 10
    return score

print(score('hello'))
print(score('stacey'))
print(score('computer'))
print(score('woop'))

