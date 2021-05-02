if __name__ == '__main__':
    n = int(input())
    ls = []
    avg = tot = 0.0
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ls = student_marks[query_name]
    for i in ls:
        tot = tot + i
    avg = tot / 3
    print("{:.2f}".format(avg))
