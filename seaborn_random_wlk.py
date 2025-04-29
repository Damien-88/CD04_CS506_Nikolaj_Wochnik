import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from random_walk import RandomWalk

# Generate random walk
rw = RandomWalk()
rw.fill_walk()

# Create Seaborn DataFrame w/ Pandas
df = pd.DataFrame({
    "x": rw.x_values,
    "y": rw.y_values,
})

# Plot using seaborn.lineplot()
# Set Seaborn plots theme
sns.set_theme(style = "whitegrid")

# Create new figure w/ specific size
plt.figure(figsize = (10, 6))

# Plot random walk data w/ Seaborn lineplot
sns.lineplot(data = df, x = "x", y = "y")

# Define margins for axes
x_margin = 5
y_margin = 5

# Set x-axis limit w/ defined margin
plt.xlim(df["x"].min() - x_margin, df["x"].max() + x_margin)

# Set y-axis limit w/ defined margin
plt.ylim(df["y"].min() - y_margin, df["y"].max() + y_margin)

# Add title w/ a specific font size
plt.title("Seaborn Random Walk", fontsize = 16)

# Label x-axis w/ padding for readability
plt.xlabel("X", labelpad = 20)

# Label y-axis w/ padding & rotate for readability
plt.ylabel("Y", rotation = 0, labelpad = 15)

# Display plot
plt.show()