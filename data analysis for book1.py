import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('data.csv')

# Group by Region and sum the Sales
region_sales = df.groupby('Region')['Sales'].sum()

# Print the grouped data
print("Total Sales by Region:")
print(region_sales)

# Plot the results
region_sales.plot(kind='bar', title='Total Sales by Region', ylabel='Sales', xlabel='Region', color='skyblue')
plt.tight_layout()
plt.show()
