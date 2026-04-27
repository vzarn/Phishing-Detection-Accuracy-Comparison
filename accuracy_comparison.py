import matplotlib.pyplot as plt

# Algorithms and reported accuracy values
algorithms = [
    "Decision Tree",
    "Random Forest",
    "SVM",
    "Logistic Regression",
    "Naive Bayes"
]

accuracy_study_1 = [96.0, 97.3, 95.8, 94.2, 93.5]
accuracy_study_2 = [96.3, 97.1, 93.9, 92.7, 60.1]

# X-axis positions
x = range(len(algorithms))
bar_width = 0.35

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(
    [i - bar_width / 2 for i in x],
    accuracy_study_1,
    width=bar_width,
    label="Study 1"
)

plt.bar(
    [i + bar_width / 2 for i in x],
    accuracy_study_2,
    width=bar_width,
    label="Study 2"
)

# Add value labels
for i, value in enumerate(accuracy_study_1):
    plt.text(
        i - bar_width / 2,
        value + 0.5,
        f"{value}%",
        ha="center",
        fontsize=9
    )

for i, value in enumerate(accuracy_study_2):
    plt.text(
        i + bar_width / 2,
        value + 0.5,
        f"{value}%",
        ha="center",
        fontsize=9
    )

# Chart details
plt.title("Accuracy Comparison of ML Algorithms for Phishing Website Detection")
plt.xlabel("Machine Learning Algorithms")
plt.ylabel("Accuracy (%)")

plt.xticks(x, algorithms, rotation=20)
plt.ylim(50, 100)

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.legend()

# Save chart as image
plt.savefig("ml_accuracy_comparison.png", dpi=300, bbox_inches="tight")

# Display chart
plt.show()
