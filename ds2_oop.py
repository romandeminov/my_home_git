import time


def fun_decorator(funk):
    def wrapper_funk(*args, **kwargs):
        time_start = time.time()
        fun_start = int(input('Введите начало диапозона для поиска'))
        fun_end = int(input('Введите конец диапозона для поска'))
        if fun_start > fun_end:
            fun_start, fun_end = fun_end, fun_start
        print(funk(fun_start, fun_end))
        time_end = time.time()
        return f'время на выполнение скрипта = {time_end - time_start}'
    return wrapper_funk


@fun_decorator
def simple_digits(start, end):
    plist = [i for i in range(start, end)]
    new_list = []
    for i in plist:
        counter = 0
        for j in plist:
            if i % j == 0:
                counter += 1
        if counter == 2:
            new_list.append(i)
    return f"простые числа в диапазоне - {new_list}"


print(simple_digits())