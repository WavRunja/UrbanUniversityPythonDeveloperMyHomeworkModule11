# module_11_1.py

# Домашнее задание по теме "Обзор сторонних библиотек Python".

# requests - запросить данные с сайта и вывести их в консоль.
import requests

# Запрос данных с сайта

response = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre/')
# Преобразуем данные в формат JSON
data = response.json()

# Выводим первый жанр
for post in data[:10]:
    while post != ' ':
        print(post, end='')
        break
print()

# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
import pandas as pd

# Создаем DataFrame
data = {
    # 'Character`s_name'
    'Имя персонажа': ['Доктор Ливси', 'Джон Сильвер', 'Джим Хокинс', 'Сквайр Трелони'],
    # 'Age'
    'Возраст': [49, 50, 15, 52],
    # 'City'
    'Место жительства': ['Бристоль', 'Портсмут', 'Адмирал Бенбоу', 'Бристоль'],
    # 'Description'
    'Описание':
        ['Очень хороший и весёлый человек.',
        'Самый страшный пират, но притворяется добрым.',
        'Очень, очень хороший и вежливый мальчик.',
        'Туп, жаден, прожорлив, надменен, трусоват, ленив.'],
    # 'Character'
    'Характер': ['Общительный', 'Скрытный', 'Мягкий', 'Отсутствует'],
    # 'Marital_status'
    'Семейное положение': ['Не женат', 'Не женат', 'Не женат', 'Не женат'],
}

df = pd.DataFrame(data)

# Устанавливаем параметр для отображения всех столбцов
pd.set_option('display.max_columns', None)


# Выводим первые несколько строк
print("COPM for Treasure Island")
print(df.head())

# Выполняем анализ данных: Средний возраст
# Для вычисления среднего значения в pandas, используем функцию mean() .
average_age = df['Возраст'].mean()
print(f"\nСредний возраст: {average_age:.2f}")

# Группируем по месту жительства и считаем количество людей
city_counts = df['Место жительства'].value_counts()
print("\nКоличество людей по месту жительства:")
print(city_counts)

# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
import matplotlib.pyplot as plt
import math
import scipy


# Создаем данные для графиков
x0 = [1, 2, 3, 4, 5]
y0 = [2, 3, 5, 7, 11]

x1 = []
y1 = []
for i in range(-5, 6):
    x1.append(i)
    y1.append(i**2)
    # print(x1)
    # print(y1)

x2 = [i for i in range(-5, 6)]
y2 = [10*(1/(1 + math.exp(-i))) for i in range(-5, 6)]

y3 = [20*scipy.special.expit(i) for i in range(-5, 6)]

# Создаем графики
plt.plot(x0, y0, marker='o', linestyle='-', color='b')
plt.plot(x1, y1, marker='o', linestyle='-.', color='g')
plt.plot(x2, y2, marker='o', linestyle=':', color='r')
plt.plot(x2, y3, marker='o', linestyle='--', color='y')

# '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# Добавляем заголовок и метки осей
plt.title('Построение графиков функций')
plt.xlabel('Ось абсцисс - Ox')
plt.ylabel('Ось ординат - Oy')

# Отображаем графики
plt.show()
