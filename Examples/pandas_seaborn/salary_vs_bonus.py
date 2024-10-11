'''
Создайте точечный график, где по оси X будет отображаться зарплата (salary), а по
оси Y — бонусы (bonus). Размер точек на графике должен быть пропорционален
количеству лет в компании (years_at_company). Этот график позволит исследовать
взаимосвязь между зарплатой и бонусами и оценить влияние стажа на размер
бонусов.
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.isnull().sum()
sns.scatterplot(data = df, x = 'salary', y = 'bonus', size = 'years_at_company')
plt.title('Salary vs Bonus with Years at Company')
plt.xlabel('Salary')
plt.ylabel('Bonus')