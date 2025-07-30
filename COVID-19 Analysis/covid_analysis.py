import pandas as pd


data = pd.read_csv("country_wise_latest.csv", delimiter=',')  

print(data.head())

#   
print(data.columns)

# حساب معدل الوفيات والتعافي لكل دولة
data['Death Rate (%)'] = (data['Deaths'] / data['Confirmed']) * 100
data['Recovery Rate (%)'] = (data['Recovered'] / data['Confirmed']) * 100

# عرض الدول ذات أعلى معدل وفيات
top_death_rates = data.sort_values('Death Rate (%)', ascending=False).head(10)
print(top_death_rates[['Country/Region', 'Death Rate (%)']])


import matplotlib.pyplot as plt

# أعلى 10 دول في معدل الوفيات
top_death_rates.head(10).plot.bar(x='Country/Region', y='Death Rate (%)', color='red')
plt.title('أعلى 10 دول في معدل الوفيات')
plt.xticks(rotation=45)
plt.show()

# الدول ذات أكبر زيادة أسبوعية
top_increase = data.sort_values('1 week % increase', ascending=False).head(5)
print(top_increase[['Country/Region', '1 week % increase']])
