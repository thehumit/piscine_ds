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

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    time_append = timeit.timeit(lambda: appender(emails), number = 100000)
    time_comrehension = timeit.timeit(lambda: comprehensor(emails), number = 100000)
    time_map = timeit.timeit(lambda: mapper(emails), number = 100000)
    time_dict = {
        "append" : time_append,
        "list comprehension" : time_comrehension,
        "map" : time_map
    }
    print(f"It is better to use {min(time_dict, key=time_dict.get)}")
    sorted_time = sorted(time_dict.values())
    print(f"{sorted_time[0]} vs {sorted_time[1]} vs {sorted_time[2]}")


if __name__ == "__main__":
    main()
