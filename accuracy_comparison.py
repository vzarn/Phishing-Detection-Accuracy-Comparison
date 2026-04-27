import matplotlib.pyplot as plt

# Data
media_agencies = [5, 10, 15, 20]

centralized_fl = [97.58, 96.8, 95.23, 93.51]
decentralized_fl = [97.3, 96.57, 95.09, 93.12]

# Create chart
plt.figure(figsize=(6, 4))

plt.plot(
    media_agencies,
    centralized_fl,
    marker='o',
    label='Centralized FL'
)

plt.plot(
    media_agencies,
    decentralized_fl,
    marker='o',
    label='Decentralized FL'
)

# Add value labels
for x, y in zip(media_agencies, centralized_fl):
    plt.text(x, y + 0.15, str(y), ha='center', fontsize=8)

for x, y in zip(media_agencies, decentralized_fl):
    plt.text(x, y - 0.35, str(y), ha='center', fontsize=8)

# Chart labels
plt.title('Accuracy Comparison')
plt.xlabel('Number of Media Agency')
plt.ylabel('Accuracy (%)')

# Axis range
plt.ylim(86, 100)

# Grid and legend
plt.grid(True)
plt.legend()

# Save image
plt.savefig('accuracy_comparison.png', dpi=300, bbox_inches='tight')

# Show chart
plt.show()
