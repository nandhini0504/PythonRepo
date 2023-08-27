def disjoint(s,x,y):
    a=set(x)
    b=set(y)
    happiness=0
    for i in s:
        if i in x:
            happiness += 1
        if i in y:
            happiness -= 1
    print(happiness)
    return happiness