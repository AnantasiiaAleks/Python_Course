'''
Постройте линейный график, где по оси X будет отображаться возраст (age), а по оси
Y — балл по расходам (spending_score). Этот график поможет визуализировать, как
изменяются расходы в зависимости от возраста сотрудников. Проанализируйте тренды
и выявите возможные закономерности.
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
sns.lineplot(data = df, x = 'age', y = 'spending_score')
plt.title('Age vs Spending Score')
plt.xlabel('Age')
plt.ylabel('Spending Score')