import timeit

from numpy import number

def appender(x):
    new_list = []
    for i in x * 5:
        if i.find("@gmail.com") != -1:
            new_list.append(i)
    return (new_list)

def comprehensor(x):
    new_list = [i for i in x * 5 if i.find("@gmail.com") != -1]
    return (new_list)

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    time_append = timeit.timeit(lambda: appender(emails), number = 100000)
    time_comrehension = timeit.timeit(lambda: comprehensor(emails), number = 100000)
    if (time_comrehension <= time_append):
        print("It is better to use list comprehension")
        print(f"{time_comrehension} vs {time_append}")
    else:
        print("It is better to append to list")
        print(f"{time_append} vs {time_comrehension}")



if __name__ == "__main__":
    main()

