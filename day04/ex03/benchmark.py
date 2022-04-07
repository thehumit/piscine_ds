import sys


import sys
import timeit
from functools import reduce

def loop_square(x):
    sum = 0
    for i in range(x):
        sum += i * i
    return (sum)

def reduce_square(x):
    sum_to_ret = reduce(lambda sum, y: sum + y * y, range(x))
    return (sum_to_ret)

def main():

    time_dict = {
        "loop" : loop_square,
        "reduce" : reduce_square
    }
    try:
        print(timeit.timeit(lambda: time_dict[sys.argv[1]](int(sys.argv[3])), number = int(sys.argv[2])))
    except (KeyError):
        pass
    

if __name__ == "__main__":
    if len(sys.argv) == 4:
        main()