import matplotlib.pyplot as plt

# Data
strategies = ['Random LB', 'Round Robin LB', 'S$_{URA}$ LB']
coeff_variation = [59.6, 55.3, 22.3]

# Plotting the data
plt.figure(figsize=(8, 6))
bars = plt.bar(strategies, coeff_variation, color='blue')

# Adding title and labels
plt.title('Coefficient variation of packet loss')
plt.xlabel('Load Balancing Strategy')
plt.ylabel('Coefficient variation [%]')

# Adding the percentage values on top of the bars
for bar, value in zip(bars, coeff_variation):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 1, f'{value}%', ha='center', color='black', fontsize=11)

# Showing the plot
plt.show()
