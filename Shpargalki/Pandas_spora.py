# 1. Импорт библиотеки:
import pandas as pd

# 2. Создание DataFrame:
data = {'column1': [1, 2], 'column2': [3, 4]}
df = pd.DataFrame(data)

# 3. Чтение данных:
# - Из CSV файла:
df = pd.read_csv('file.csv')
# - Из Excel файла:
df = pd.read_excel('file.xlsx')

# 4. Основные операции:
# - Просмотр первых n строк:
df.head(n)
# - Просмотр последних n строк:
df.tail(n)

# 5. Информация о DataFrame:
# - Основана статистика:
df.describe()
# - Информация о DataFrame:
df.info()

# 6. Индексация и выбор данных:
# - Выбор столбца:
df['column1']
# - Выбор строки по индексу:
df.iloc[0]  # по позиции
df.loc[index]  # по индексу

# 7. Фильтрация данных:
filtered_df = df[df['column1'] > 1]

# 8. Сортировка:
# - По одному столбцу:
df.sort_values(by='column1')
# - По нескольким столбцам:
df.sort_values(by=['column1', 'column2'], ascending=[True, False])

# 9. Добавление и удаление столбцов:
# - Добавление столбца:
df['new_column'] = value
# - Удаление столбца:
df.drop('column_name', axis=1, inplace=True)

# 10. Объединение и конкатенация:
-#  Конкатенация:
result = pd.concat([df1, df2])
# - Объединение по ключу:
result = pd.merge(df1, df2, on='key')

# 11. Группировка:
grouped = df.groupby('column_name').sum()

# 12. Применение функций:
df['column'].apply(lambda x: x + 1)

# 13. Проверка на наличие пропусков:
df.isnull().sum()

# 14. Заполнение пропусков:
df.fillna(value)

# 15. Сохранение DataFrame:
# - В CSV файл:
df.to_csv('output.csv', index=False)

# - В Excel файл:
df.to_excel('output.xlsx', index=False)

