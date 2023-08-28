def list_new(i): # By defining a function, you can reuse this code easily and make your code more organized and readable.defined to take one argument, which is denoted by the variable i
    mylist = [] # empty list is initialised
    for x in i:   #splits the command string x into a list of words. For example, if x is 'insert 0 5', then s becomes ['insert', '0', '5']
        s = x.split()
        if s[0] == 'insert': #inserts an element at the specified position.
            mylist.insert(int(s[1]), int(s[2]))
        elif s[0] == 'remove': #removes an element from the list.
            mylist.remove(int(s[1]))
        elif s[0] == 'append':   #appends an element to the end of the list.
            mylist.append(int(s[1]))
        elif s[0] == 'sort':    #sorts the list.
            mylist.sort()
        elif s[0] == 'pop':    #removes the last element from the list
            mylist.pop()
        elif s[0] == 'reverse':  #reverses the list
            mylist.reverse()
        elif s[0] == 'print':   #prints the current state of the list
            print(mylist)

    return mylist         #By returning mylist, the function allows the caller to access the modified list after the commands have been processed.