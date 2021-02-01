
from datetime import datetime

# Complete the time_delta function below.


def time_delta(t1, t2):

    f = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, f)
    t2 = datetime.strptime(t2, f)
    diff = (t2-t1).total_seconds()
    print(abs(int(diff)))
    return abs(int(diff))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta))
        fptr.write('\n')
    fptr.close()
