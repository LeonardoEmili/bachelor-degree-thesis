#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Names and labels
types = ["energy", "latency", "pdr", "overhead"]
labels = ["Energy spent by the network [J]", "Latency [ms]", "Packet delivery ratio", "Packets overhead"]

# Choose a value:
# 0 - energy
# 1 - latency
# 2 - pdr
# 3 - overhead
m_type = 0

# Raw data to plot (parsed from GC simulations)
n = 140
energy1 = [x*n for x in [38.46007, 16.37003, 9.12696, 4.64407, 3.13403]]
energy2 = [x*n for x in [33.60001, 14.31184, 8.14755, 4.2216, 2.92407]]
latency1 = [392.87577, 386.10047, 385.0174, 382.8534, 380.6449]
latency2 = [382.4569, 373.7848, 374.4934, 372.6346, 376.6205]
pdr1 = [99.665, 99.833, 99.956, 99.96, 99.868]
pdr2 = [99.512, 99.662, 99.696, 99.766, 99.821]
overhead1 = [x/100 for x in [22.3, 22.2, 22.6, 22.3, 22.0]]
overhead2 = [x/100 for x in [17.8, 17.8, 18.1, 17.8, 16.5]]

base_protocol = [energy1, latency1, pdr1, overhead1]
variant_protocol = [energy2, latency2, pdr2, overhead2]

bars1 = base_protocol[m_type]
bars2 = variant_protocol[m_type]

# Set width of bar
barWidth = 0.25

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

# Make the plot
plt.bar(r1, bars1, color='#388e3c', width=barWidth,
        edgecolor='white', label='GREEN-WUP')
plt.bar(r2, bars2, color='#039be5', width=barWidth,
        edgecolor='white', label='VARIANT')

# Add xticks on the middle of the group bars
plt.ylabel(labels[m_type], fontsize=12)
plt.xlabel('iaTime', fontsize=12)
plt.xticks([r + barWidth/2 for r in range(len(bars1))],
           ['2', '5', '10', '25', '50'])

# Display values as percentages only if required
if types[m_type] == "overhead":
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

plt.locator_params(axis='y', nbins=6)

# Create legend & Show graphic
plt.legend(loc="upper right")
# plt.show()
plt.savefig('../assets/' + types[m_type] + '_plot.png')
plt.close()
