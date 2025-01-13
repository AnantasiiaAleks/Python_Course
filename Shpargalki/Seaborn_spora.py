#1. Импорт библиотеки:
import seaborn as sns
import matplotlib.pyplot as plt

#2. Основные команды для построения графиков:
#- Линейный график:
sns.lineplot(x='column_x', y='column_y', data=data)
plt.title('Линейный график')
plt.show()

#- Гистограмма:
sns.histplot(data, x='column', bins=10)
plt.title('Гистограмма')
plt.show()

#- Коэффициент ядерной плотности (KDE):
sns.kdeplot(data=data, x='column')
plt.title('KDE график')
plt.show()

#- Диаграмма рассеяния:
sns.scatterplot(x='column_x', y='column_y', data=data, hue='category')
plt.title('Диаграмма рассеяния')
plt.show()

#- Ящик с усами (Box plot):
sns.boxplot(x='category', y='value', data=data)
plt.title('Ящик с усами')
plt.show()

#3. Настройки графиков:
#- Добавление легенды:
sns.scatterplot(x='column_x', y='column_y', data=data, hue='category', style='style_column')

#- Группировка по категориям:
sns.catplot(x='category', y='value', data=data, kind='bar')

#4. Настройка внешнего вида:
#- Применение стиля:
sns.set_style('whitegrid')  # Применение стиля

#- Установка палитры:
sns.set_palette('pastel')  # Выбор палитры

#5. Сохранение графиков:
plt.savefig('seaborn_plot.png', format='png')

#6. Дополнительные типы графиков:
#- Тепловая карта (heatmap):
sns.heatmap(data.corr(), annot=True, fmt=".2f")
plt.title('Тепловая карта')
plt.show()

#- Параллельные координаты:
sns.pairplot(data)
plt.title('Параллельные координаты')
plt.show()