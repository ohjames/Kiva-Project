import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
import matplotlib.ticker as mtick

df = pd.read_csv('kiva_data.csv')
print(df.columns)
print(df.head())

f, ax = plt.subplots(figsize = (15,10))
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
sns.set_palette('Dark2')
sns.set_style(('darkgrid'))
plt.figure(figsize=(25, 15))
plt.title('Average Loan Amounts ($USD) Given from Kiva by gender and country')
sns.barplot(data = df, x = 'country', y = 'loan_amount', hue = 'gender')
plt.show()
plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x = 'country', y = 'loan_amount')
plt.show()
plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x = 'activity', y = 'loan_amount')
plt.show()
plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x = 'activity', y = 'loan_amount')
plt.show()
plt.figure(figsize=(16, 10))
sns.set_palette('Spectral')
sns.violinplot(data=df, x = 'country', y = 'loan_amount', hue = 'gender', split = True)
plt.show()
#todo clean up graph labels