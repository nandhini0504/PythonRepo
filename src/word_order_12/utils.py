def word_order(n,i):
    d = {}
    l = []
    for i in range(n):
        a = input()
        l.append(a)
        if a in d:
            count[a] += 1
        else:
            d[a] = 1

    return (len(d))
    return ' '.join([str(a) for i in d])