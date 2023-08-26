def merge_the_tools(string, k):
    lis=[]
    for i in range(int(len(string) / k)):
        str =''
        for j in range(k):
            if string[i * k + j] not in str:
                str = str+(string[i * k + j])
        lis.append(str)
    print(lis)
    return lis
