import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("mahindra_and_mahindra_bal.csv")

corr = df.corr(numeric_only=True).round(2)

print(corr.to_string())

plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    square=True
)

plt.title("Correlation Heatmap")

plt.show()