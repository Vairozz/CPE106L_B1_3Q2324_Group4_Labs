import pandas as pd
import matplotlib.pyplot as plt

filename = 'breadprice.csv'
df = pd.read_csv(filename)

df = df.ffill(axis=1)

df['Avg_Price'] = df.mean(axis=1)

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Avg_Price'], marker='o', linestyle='-')
plt.title('Average Bread Price Over Years')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()
