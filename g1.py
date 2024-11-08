import matplotlib.pyplot as plt

# Data
attackers = [0, 2, 4, 6, 8, 10]
random_lb = [1.5, 2.2, 2.8, 3.1, 3.3, 3.7]
round_robin_lb = [1.5, 1.8, 2.3, 2.6, 2.9, 3.2]
s_ura_lb = [1.5, 1.6, 1.8, 2.0, 2.1, 2.4]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(attackers, random_lb, marker='^', linestyle='-', color='blue', label='Random LB')
plt.plot(attackers, round_robin_lb, marker='o', linestyle='-', color='dodgerblue', label='Round Robin LB')
plt.plot(attackers, s_ura_lb, marker='s', linestyle='-', color='black', label='S$_{URA}$ LB')

# Adding titles and labels
plt.title('Packet Loss comparison - Under Attack')
plt.xlabel('Number of attackers')
plt.ylabel('Packet Loss [%]')
plt.xticks(attackers)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend()

# Showing the plot
plt.show()
