import pandas as pd
import matplotlib.pyplot as plt
from data import games

attendance = games.loc[games['type'] == 'info' and games['multi2'] == 'attendance', ['year', 'multi3']]
attendance.columns = ['year', 'attendance']
attendance.loc[:, 'attendance'] = pd.numeric(attendance.loc[:, 'attendance'])
plt.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.show(plt.xlabel('Year'), plt.ylabel('Attendance'))
plt.axhline(attendance['column'].mean(), plt.axhline(): label, linestyle, color)

