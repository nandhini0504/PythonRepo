def second_max_number(n,arr):
    output = sorted(set(arr), reverse=True)[1]
    print(output)
    return output