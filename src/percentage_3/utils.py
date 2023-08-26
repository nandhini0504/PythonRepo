def percentage_calculation(student_mark,name):
    n = len(student_mark[name])
    total =0
    for i in range(n):
        total = total +student_mark[name][i]
    avg = total /n
    return avg