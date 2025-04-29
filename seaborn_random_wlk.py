import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from random_walk import RandomWalk

# Generate random walk
rw = RandomWalk()
rw.fill_walk()

# Create a DataFrame for Seaborn
df = pd.DataFrame({
    "x": rw.x_values,
    "y": rw.y_values,
})

# Plot using seaborn.lineplot()
sns.set_theme(style = "whitegrid")
plt.figure(figsize = (10, 6))
sns.lineplot(data = df, x = "x", y = "y",)
x_margin = 5
y_margin = 5
plt.xlim(df["x"].min() - x_margin, df["x"].max() + x_margin)
plt.ylim(df["y"].min() - y_margin, df["y"].max() + y_margin)
plt.title("Seaborn Random Walk", fontsize = 14)
plt.xlabel("X", labelpad = 20)
plt.ylabel("Y", rotation = 0, labelpad = 15)
plt.axis("equal")
plt.show()