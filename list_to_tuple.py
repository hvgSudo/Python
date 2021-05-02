if __name__ == '__main__':
    n = int(input())
    integer_list = c = []
    b = input()
    c = b.split(" ")
    print(c)
    for i in c:
        integer_list.append(int(i))
    print(integer_list)
    a = tuple(integer_list)
    print(a)
    print(hash(a))
