def data_type():
    str_value = 1
    int_value = "a"
    float_value = 1.1
    bool_value = True
    list_value = []
    dict_value = {"dict":1}
    tuple_value = ()
    set_value = {1, 2, 3, 4}
    for i in (str_value, int_value, float_value, bool_value, list_value, dict_value, tuple_value, set_value):
        list_value.append(type(i).__name__)
    print(list_value)

if __name__ == '__main__':
    data_type()
