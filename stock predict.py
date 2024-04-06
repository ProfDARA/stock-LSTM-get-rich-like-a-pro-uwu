import pandas as pd
import datetime
import matplotlib.pyplot as plt

# read csv
df = pd.read_csv('MSFT.csv')

# selektor date dan close
df = df[['Date', 'Close']]

# fungsi konversi string to date
def string_to_date(s):
    split = s.split('-')
    year, month, day = int(split[0]), int(split[1]), int(split[2])
    return datetime.datetime(year=year, month=month, day=day)

# apply string to date
df['Date'] = df['Date'].apply(string_to_date)

# St date ke index
df.set_index('Date', inplace=True)

# Plotting
plt.plot(df['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('MSFT Close Price Over Time')
plt.show()
