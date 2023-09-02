import datetime
def read_datetime():
    return datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
def main():
    time = int(input())
    for _ in range(time):
        t1 = read_datetime()
        t2 = read_datetime()

        print(int(abs(t1 - t2).total_seconds()))

    if __name__ == '__main__':
        main()
