def score_game(any_number=0):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count = 1
        predict = 100/2
        suma = 50
        while number != predict:
            count+=1
            if number > predict:
                predict = predict + math.ceil(suma)
                suma /= 2
            elif number < predict:
                predict = predict-math.ceil(suma)
                suma /= 2
        count_ls.append(count)
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
score_game()
