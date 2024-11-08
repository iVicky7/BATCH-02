import matplotlib.pyplot as plt
import numpy as np
# Data
labels = ['1 IDS-enabled', '2 IDS-enabled', '3 IDS-enabled', '4 IDS-enabled', '5 IDS-enabled']
without_lb = [4.5, 0, 0, 0, 0]  # example data
random_lb = [0, 4.2, 3.4, 3.1, 2.9]  # example data
round_robin_lb = [0, 0, 3.7, 2.4, 1.8]  # example data
s_ura_lb = [0, 0, 2.8, 2.0, 1.4]  # example data
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - 1.5*width, without_lb, width, label='Without LB', color='blue')
rects2 = ax.bar(x - 0.5*width, random_lb, width, label='Random LB', color='orange')
rects3 = ax.bar(x + 0.5*width, round_robin_lb, width, label='Round Robin LB', color='yellow')
rects4 = ax.bar(x + 1.5*width, s_ura_lb, width, label='S_URA LB', color='purple')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Packet Loss [%]')
ax.set_title('Packet Loss using different load balancing strategies')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.legend()
# Add annotations
def autolabel(rects):
    """Attach a text label above each bar in rects, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

plt.show()