# Making necessary imports
import pandas as pd
import matplotlib.pyplot as plt
from config import file_path, sheet_name

# Loading data from Excel file
df = pd.read_excel(file_path, sheet_name)

# Displaying the first few rows of the dataset for a quick overview
print(df.head())

# Ploting the checkout process steps over time for visualization
df.plot(x='event_weekbeg', y=['checkout_start', 'ship_method_success', 'payment_info_success', 'place_order_start', 'place_order_success', 'place_order_error'], marker='o')
plt.title('Checkout Process Over Time')
plt.xlabel('Week')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
