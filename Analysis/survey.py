import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("survey.csv")

# Satisfaction Levels
satisfaction_counts = df["Satisfaction"].value_counts()

# Order
order = ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]

# Reindex for correct order
satisfaction_counts = satisfaction_counts.reindex(order)

# Calculate percentages
total = satisfaction_counts.sum()
percentages = (satisfaction_counts / total) * 100

# Style
sns.set_style("whitegrid")

# Plot
plt.figure(figsize=(9,5))
bars = sns.barplot(
    x=satisfaction_counts.index,
    y=satisfaction_counts.values,
    hue=satisfaction_counts.index,  
    palette="viridis",
    legend=False
)

# Labels inside bars
for i, (count, percent) in enumerate(zip(satisfaction_counts.values, percentages)):
    plt.text(i, count/2, f"{int(count)} ({percent:.1f}%)", 
             ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Labels and title
plt.title("Survey Results: Satisfaction Levels", fontsize=18)
plt.xlabel("Satisfaction Level", fontsize=14)
plt.ylabel("Number of People", fontsize=14)

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()