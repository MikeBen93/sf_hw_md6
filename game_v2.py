import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    range_from =1 
    range_to = 101
    count = 0

    predict_number = np.random.randint(range_from, range_to) # предполагаемое число
    # цикл для проверки угадывания
    while True:
        count += 1
        # в условиях ниже переопределяем границы, если не попали или заканчиваем цикл
        if number < predict_number:
            range_to = predict_number
        elif number > predict_number:
            range_from = predict_number
        elif number == predict_number:
            break # выход из цикла, если угадали
        # выбор случайно числа из нового промежутка
        predict_number = np.random.randint(range_from, range_to)
    return(count)

print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)