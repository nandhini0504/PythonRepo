def list_new(i):
    mylist = []
    for x in i:
        s = x.split()
        if s[0] == 'insert':
            mylist.insert(int(s[1]), int(s[2]))
        elif s[0] == 'remove':
            mylist.remove(int(s[1]))
        elif s[0] == 'append':
            mylist.append(int(s[1]))
        elif s[0] == 'sort':
            mylist.sort()
        elif s[0] == 'pop':
            mylist.pop()
        elif s[0] == 'reverse':
            mylist.reverse()
        elif s[0] == 'print':
            print(mylist)

    return mylist