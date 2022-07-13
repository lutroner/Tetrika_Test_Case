# Решение задачи 1
# Вариант_1
def task(array: str) -> str:
    return f"OUT: {array.index('0')}"


# Вариант_2
def task1(array: str) -> str:
    for i, item in enumerate(array):
        if item == '0':
            return f'OUT: {i}'


print(task1("111111111110000000000000000"))
