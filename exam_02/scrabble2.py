def score(s):
    dict = {"a,e,i,o,u,l,n,r,s,t": 1, "d,g": 2, "b,c,m,p": 3, "f,h,v,w,y": 4, "k": 5, "j,x":8, "q,z": 10}
    score= 0
    for char in dict:
        for key in dict:
            if char in key:
                score+=dict[key]
    return score

print(score('hello'))
print(score('stacey'))
print(score('computer'))
print(score('woop'))

