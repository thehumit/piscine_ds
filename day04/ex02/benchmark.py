import sys
import timeit

def appender(x):
    new_list = []
    for i in x * 5:
        if i.find("@gmail.com"):
            new_list.append(i)
    return (new_list)

def comprehensor(x):
    new_list = [i for i in x * 5 if i.find("@gmail.com")]
    return (new_list)

def mapper(x):
    new_list = list(map(lambda  y: y if y.find("@gmail.com") != -1 else None, x * 5))
    return (new_list)

def filterer(x):
    new_list = list(filter(lambda y: y if y.find("@gmail.com") != -1 else False, x * 5))
    return (new_list)

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    time_dict = {
        "loop" : appender,
        "list_comprehension" : comprehensor,
        "map" : mapper,
        "filter" : filterer
    }
    try:
        print(timeit.timeit(lambda: time_dict[sys.argv[1]](emails), number = int(sys.argv[2])))
    except (KeyError):
        pass
    


if __name__ == "__main__":
    if (len(sys.argv) == 3):
        main()
