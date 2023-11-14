# Making necessary imports
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns
from config import file_path, sheet_name

# Loading data from Excel file
df = pd.read_excel(file_path, sheet_name)

# Selecting columns for correlational analysis
columns_to_analyze = ['checkout_start', 'ship_method_success', 'payment_info_success', 'place_order_start', 'place_order_success', 'place_order_error']

# Calculating correlation matrix
correlation_matrix = df[columns_to_analyze].corr()

# Displaying the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Ploting a heatmap of the correlation matrix for visualization 
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
