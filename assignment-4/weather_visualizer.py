import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv("daily_weather_data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())



df['date'] = pd.to_datetime(df['date'], errors='coerce')


df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())
df['rainfall'] = df['rainfall'].fillna(0)


df = df[['date', 'temperature', 'humidity', 'rainfall']]



daily_mean_temp = np.mean(df['temperature'])
max_temp = np.max(df['temperature'])
min_temp = np.min(df['temperature'])

print("\nDaily Mean Temperature:", daily_mean_temp)
print("Max Temperature:", max_temp)
print("Min Temperature:", min_temp)


df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year


plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("daily_temperature.png")
plt.show()


monthly_rainfall = df.groupby('month')['rainfall'].sum()

plt.figure(figsize=(10, 5))
monthly_rainfall.plot(kind='bar')
plt.title("Monthly Rainfall Totals")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("monthly_rainfall.png")
plt.show()


plt.scatter(df['humidity'], df['temperature'])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity (%)")
plt.ylabel("Temperature (°C)")
plt.savefig("humidity_vs_temperature.png")
plt.show()


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(df['date'], df['temperature'], color='blue')
plt.title("Temperature Trend")

plt.subplot(1, 2, 2)
plt.scatter(df['humidity'], df['temperature'], color='green')
plt.title("Humidity vs Temp")

plt.savefig("combined_plot.png")
plt.show()



month_group = df.groupby('month').agg({
    'temperature': 'mean',
    'rainfall': 'sum',
    'humidity': 'mean'
})

print("\nMonthly Summary:")
print(month_group)



df.to_csv("cleaned_weather.csv", index=False)
month_group.to_csv("monthly_summary.csv")

print("\nAll tasks completed successfully!")
