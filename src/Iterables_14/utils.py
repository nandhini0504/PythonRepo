import itertools
def itertools_func(N,my_list,K):
    combinations = list(itertools.combinations(my_list, K))
    #print(combinations)
    count=0
    for combination in combinations:
        if 'a' in combination:
            count+=1
    probability = count / len(combinations)
    print(float(format(probability,'.3f')))
    return(float(format(probability,'.3f')))