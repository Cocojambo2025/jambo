"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def limits_predict(number: int = 1) -> int:
    """Угадываем число с помощью сжатия границ поиска и исключения повторных предположений

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    low_limit = 1
    up_limit = 101
    predict_list = []
    while True:
        count += 1
        x = np.random.randint(low_limit, up_limit)
        
        while x in predict_list:
            x = np.random.randint(low_limit, up_limit)
        predict_number = x
        
        if number == predict_number:
            break  # выход из цикла если угадали
        
        if number > predict_number:
            low_limit = predict_number
            
        if number < predict_number:
            up_limit = predict_number
        
        predict_list.append (predict_number)
              
    return count


def score_game(limits_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(2000))  # загадали список чисел

    for number in random_array:
        count_ls.append(limits_predict(number))

    score = int(np.mean(count_ls))
   
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток при совершении 2000 подходов")
    
    
    import matplotlib.pyplot as plt
    
    count_ls.sort()
    points_list=list(set(count_ls))
    hight_list =[]
    for elem in points_list:
         hight_list.append(count_ls.count(elem))
    
  
    plt.bar(points_list, hight_list, label='успешных попыток')
    plt.xlabel('Число итераций до угадывания')
    plt.ylabel('Количество успешных попыток')
    plt.title('Нормальное распределение количеств попыток')
    plt.legend()
    plt.show()
    
    return score


# RUN
if __name__ == "__main__":
    score_game(limits_predict)

