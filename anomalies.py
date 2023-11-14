# Making necessary imports
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt
from config import file_path, sheet_name

# Loading data from Excel file
df = pd.read_excel(file_path, sheet_name)

# Selecting columns for analysis
columns_to_analyze = ['checkout_start', 'ship_method_success', 'payment_info_success', 'place_order_start', 'place_order_success', 'place_order_error']

# Calculating z-scores for each step
df_zscore = df.copy()
for column in columns_to_analyze:
    df_zscore[column + '_zscore'] = zscore(df[column])

# Calculating the average z-score for each week
df_zscore['avg_zscore'] = df_zscore[[column + '_zscore' for column in columns_to_analyze]].mean(axis=1)

# Identifying weeks with significant anomalies
significant_anomalies = df_zscore.loc[(df_zscore[columns_to_analyze] > 2).any(axis=1)]

# Sort anomalies based on the maximum z-score across all steps
significant_anomalies['max_zscore'] = significant_anomalies[columns_to_analyze].max(axis=1)
significant_anomalies_sorted = significant_anomalies.sort_values(by='max_zscore', ascending=False)

# Displaying the top four weeks with the most significant anomalies
top_four_anomalies = significant_anomalies_sorted.head(4)
print("Top four weeks with the most significant anomalies:")
print(top_four_anomalies[['event_weekbeg', 'max_zscore']])

# Plot average z-scores over time for visualization
plt.plot(df_zscore['event_weekbeg'], df_zscore['avg_zscore'], marker='o', label='Average Z-Score')
plt.title('Average Z-Scores for Checkout Process Over Time')
plt.xlabel('Week')
plt.ylabel('Average Z-Score')
plt.xticks(df_zscore['event_weekbeg'][::int(len(df_zscore['event_weekbeg']) / 20)], rotation=45) 
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
