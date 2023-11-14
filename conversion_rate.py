# Making necessary imports
import pandas as pd
import matplotlib.pyplot as plt
from config import file_path, sheet_name

# Loading data from Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Creating a list of columns representing each step in the checkout process
checkout_steps = ['checkout_start', 'ship_method_success', 'payment_info_success', 'place_order_start', 'place_order_success', 'place_order_error']

# Calculating conversion rates for each step in the checkout process using a simple for loop
for i in range(len(checkout_steps) - 1):
    from_step = checkout_steps[i]
    to_step = checkout_steps[i + 1]
    conversion_rate_column = f'conversion_rate_{from_step}_to_{to_step}'
    df[conversion_rate_column] = df[to_step] / df[from_step] * 100

# Printing the minimum, maximum, and mean values for each conversion rate variable (this is the mean, min, and max snippets in the document)
print("Minimum Conversion Rates:")
print(df[[f'conversion_rate_{from_step}_to_{to_step}' for from_step, to_step in zip(checkout_steps, checkout_steps[1:])]].min())

print("\nMaximum Conversion Rates:")
print(df[[f'conversion_rate_{from_step}_to_{to_step}' for from_step, to_step in zip(checkout_steps, checkout_steps[1:])]].max())

print("\nMean Conversion Rates:")
print(df[[f'conversion_rate_{from_step}_to_{to_step}' for from_step, to_step in zip(checkout_steps, checkout_steps[1:])]].mean())

# Creating main graph visualization
# Ploting conversion rates over time
plt.figure(figsize=(12, 6))

# Ploting conversion rates for all variables 
for i in range(len(checkout_steps) - 1):
    conversion_rate_column = f'conversion_rate_{checkout_steps[i]}_to_{checkout_steps[i + 1]}'
    plt.plot(df['event_weekbeg'], df[conversion_rate_column], marker='o', label=f'{checkout_steps[i]} to {checkout_steps[i + 1]}')

plt.title('Conversion Rates Over Time with Min, Max, and Mean Values')
plt.xlabel('Week')
plt.ylabel('Conversion Rate (%)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
