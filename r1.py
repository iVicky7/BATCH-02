import matplotlib.pyplot as plt
import numpy as np

# Data
strategies = ['Random LB', 'Round Robin LB', 'S_URA LB']
dynamic = [15.9, 16.2, 20.2]
static = [12.5, 14.3, 17.3]

x = np.arange(len(strategies))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, dynamic, width, label='Dynamic', color='blue')
rects2 = ax.bar(x + width/2, static, width, label='Static', color='orange')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time [min]')
ax.set_title('Battery autonomy comparison under Static and Dynamic Deployment')
ax.set_xticks(x)
ax.set_xticklabels(strategies)
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

fig.tight_layout()

plt.show()