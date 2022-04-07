import timeit, random
from collections import Counter

def dict_with_loop(l):
    d = dict()
    
    for i in range(0, 101):
        d[i] = 0
    for i in l:
        d[i] += 1
    return (d)

def best_ten_list(x):
    best_ten = dict(sorted(x.items(), key=lambda item: item[1], reverse=True)[0:10])
    return (best_ten)

def count_def(l):
    d = Counter(l)
    return (d)

def best_ten_counter(x):
    return(x.most_common(10))

def main():
    l = [random.randint(0, 100) for i in range(1000000)]
    d = dict_with_loop(l)
    c = count_def(l)
    print(f"my function: {timeit.timeit(lambda: dict_with_loop(l), number = 1)}")
    print(f"Counter: {timeit.timeit(lambda: count_def(l), number = 1)}")
    print(f"My top: {timeit.timeit(lambda: best_ten_list(d), number = 1)}")
    print(f"Counter's top: {timeit.timeit(lambda: best_ten_counter(c), number = 1)}")

if __name__=="__main__":
    try:
        main()
    except:
        pass