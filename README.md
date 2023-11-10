# sf_hw_md6

# Проект "Угадай число"

## Оглавление
1. [Описание проекта](https://github.com/MikeBen93/sf_hw_md6#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
1. [Какой кейс решаем?](https://github.com/MikeBen93/sf_hw_md6#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)
1. [Этапы работы над проектом](https://github.com/MikeBen93/sf_hw_md6#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)
1. [Результат](https://github.com/MikeBen93/sf_hw_md6#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82)
1. [Выводы](https://github.com/MikeBen93/sf_hw_md6#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### Описание проекта

Угадать загаданное компьютером число за минимальное количество попыток.

### Какой кейс решаем?

Нужно написать программу, которая угадывает число за минимальное количество попыток.

**Условия кейса:**

1. Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
1. Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.

**Метрика чества:**

Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

### Этапы работы над проектом

1. Выбор алгоритма 
1. Реализация алгоритма:
    1. Выбираем случайное число из заданного промежутка и сравниваем с загаданным числом:
        - если случайное число больше загаданного, то у ранее заданного промежутка устаналиваем верхнюю границу равную случайному числу, далее повторяем с новым промежутком
        - если случайное число меньше загаданного, то у ранее заданного промежутка устаналиваем нижнюю границу равную случайному числу, далее повторяем с новым промежутком
        - если угадали, прерываем процесс

### Результат

Алгоритм угадывает число в среднем за: 8 попыток

### Выводы

Выбранный алгоритм бинарного поиска позволяет оптимального решить поставленную задачу