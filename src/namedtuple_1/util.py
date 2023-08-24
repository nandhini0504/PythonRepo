
from collections import namedtuple
def named_tuple():
    n = int(input())
    Student = namedtuple("Student", input().split())
    total = 0

    for i in range(n):
        total += int(Student(*input().split()).MARKS)

    average = total / n
    print(average)
    return average

named_tuple()