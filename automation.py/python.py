import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("mahindra_and_mahindra_bal.csv").dropna()

df = df.select_dtypes(include="number")

y = "TotalAssets"
moderator = "TAD"

explanatory = [c for c in df.columns if c not in [y, moderator]]

df["FinancialStrength"] = df[explanatory].mean(axis=1)

df["FSxTAD"] = df["FinancialStrength"] * df[moderator]

G = nx.DiGraph()

G.add_edge("FinancialStrength", "TotalAssets")
G.add_edge("TAD", "TotalAssets")
G.add_edge("FSxTAD", "TotalAssets")

pos = {
    "FinancialStrength": (0, 1),
    "TAD": (0, 0),
    "FSxTAD": (0, -1),
    "TotalAssets": (2, 0)
}

plt.figure(figsize=(8,6))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3500,
    node_color="lightgray",
    font_size=10,
    arrowsize=20
)

plt.title("SEM with TAD as Moderating Variable")

plt.show()