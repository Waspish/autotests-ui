# Функция inner_range возвращает генератор чисел от 0 до 4
def inner_range():
    for index in range(5):
        yield index


# Функция outer_range возвращает все значения генератора inner_range с помощью yield from
def outer_range():
    yield from inner_range()


for index in outer_range():
    print(index)
