# 1. Импорт библиотеки:
import matplotlib.pyplot as plt

#2. Основные команды для построения графиков:
#- Линейный график:
plt.plot(x, y)
plt.title('Заголовок графика')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()

# - Гистограмма:
plt.hist(data, bins=10)
plt.title('Гистограмма')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.show()

# - Диаграмма рассеяния:
plt.scatter(x, y)
plt.title('Диаграмма рассеяния')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()

# - Построение нескольких графиков:
plt.subplot(1, 2, 1)  # (количество строк, количество столбцов, номер графика)
plt.plot(x1, y1)
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.show()

#3. Настройки графиков:
#- Изменение стиля линий и маркеров:
plt.plot(x, y, linestyle='--', marker='o', color='r')

#- Добавление легенды:
plt.plot(x, y1, label='Линия 1')
plt.plot(x, y2, label='Линия 2')
plt.legend()

#4. Сохранение графика:
plt.savefig('graph.png', format='png')

#5. Настройка осей:
#- Установка диапазона осей:
plt.xlim(0, 10)
plt.ylim(0, 100)

# - Установка меток на осях:
plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 20, 40, 60, 80, 100])

#6. Дополнительные типы графиков:
#- Круговая диаграмма:
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Круговая диаграмма')
plt.show()

#- График с заполнением под линией:
plt.fill_between(x, y)

#7. Настройка внешнего вида:
plt.style.use('ggplot')  # Применение стиля