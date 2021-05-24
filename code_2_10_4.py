def decorator(func):
    def wrapper(*args):
        x = func(*args)
        for i in range(len(x)):
            print(f'{i + 1} - {x[i]}')
    return wrapper


@decorator
def show_even_numbers(*args):
    even_numbers_lst = []
    for i in args:
        try:
            if i % 2 == 0:
                even_numbers_lst.append(i)
        except TypeError:
            continue
    return even_numbers_lst
show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12)
