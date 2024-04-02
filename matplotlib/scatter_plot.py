import matplotlib.pyplot as plt

# Data
capabilities = ['Zero-shot', 'Reflection', 'Tool Use', 'Planning', 'Multiagent']
gpt3_percentages = [48, None, None, None, None]
gpt4_percentages = [67, None, None, None, None]

# Filter out capabilities with missing data for GPT-4
valid_capabilities = [cap for cap, val in zip(capabilities, gpt4_percentages) if val is not None]
valid_gpt3_percentages = [val for val in gpt3_percentages if val is not None]
valid_gpt4_percentages = [val for val in gpt4_percentages if val is not None]

# Create a bar chart (using valid data)
plt.figure(figsize=(10, 6))
plt.bar(valid_capabilities, valid_gpt3_percentages, width=0.4, label='GPT-3.5')
plt.bar([i + 0.4 for i in range(len(valid_capabilities))], valid_gpt4_percentages, width=0.4, label='GPT-4')

# Set labels and title
plt.xlabel('Capabilities')
plt.ylabel('Percentage (%)')
plt.title('Coding Benchmark (HumanEval)')

# Add legend
plt.legend()

# Show the chart
plt.xticks(rotation=15)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
