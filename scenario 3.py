import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/namiy/Downloads/Housing.csv")
num_df = df.select_dtypes(include=['int64', 'float64'])
corr = num_df.corr()
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()