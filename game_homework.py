import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм
     Алгоритм работает путем постоянного деления диапазона чисел пополам.
    Сначала проверяется число в середине диапазона. Если число, которое мы взяли
    больше, то это будет верхней половиной предыдущего.Если загаданное число меньше, то новый диапазон
    становится нижней половиной предыдущего диапазона.
    Процесс продолжается до тех пор, пока не будет найдено загаданное число.

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def binary_predict(number: int = 1) -> int:
    """Угадываем число, используя алгоритм бинарного поиска.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 1
    lower_bound = 1
    upper_bound = 101
    predict = (lower_bound + upper_bound) // 2
    
    while number != predict:
        count += 1
        if number > predict:
            lower_bound = predict
        elif number < predict:
            upper_bound = predict
        
        predict = (lower_bound + upper_bound) // 2

    return count

print('Run benchmarking for binary_predict: ', end='')
score_game(binary_predict)
