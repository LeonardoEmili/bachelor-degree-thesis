#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Choose a value:
# 0 - energy
# 1 - latency
# 2 - pdr
# 3 - overhead
m_type = 0

# Select if plotting simulation with interest dissemination phase
interest_active = True

# Names and labels
types = ["energy", "latency", "pdr", "overhead"]
labels = ["Energy spent by the network [J]", "Latency [ms]", "Packet delivery ratio", "Packets overhead"]
filename = types[m_type] + '_plot.png'
if interest_active:
	filename = "interest_" + filename

# Raw data to plot (parsed from GC simulations) - CtsMaxJitter = 100
n = 140
energy1 = [x*n for x in [37.73876, 16.07003, 8.88417, 4.47382, 3.13403]]
energy2 = [x*n for x in [33.60001, 14.31184, 8.14755, 4.2216, 2.92407]]
latency1 = [392.87577, 386.10047, 385.0174, 382.8534, 380.6449]
latency2 = [382.4569, 373.7848, 374.4934, 372.6346, 376.6205]
pdr1 = [99.665, 99.833, 99.956, 99.96, 99.868]
pdr2 = [99.512, 99.662, 99.696, 99.766, 99.821]
overhead1 = [x/100 for x in [22.3, 22.2, 22.6, 22.3, 22.0]]
overhead2 = [x/100 for x in [17.8, 17.8, 18.1, 17.8, 16.5]]

# Data from simulation with dissemination active
i_energy1 = [x*n for x in [38.44381, 16.35294, 9.149, 4.56977, 3.08084]]
i_energy2 = [x*n for x in [34.49227, 14.65808, 8.32379, 4.26025, 2.93325]]

# CtsMaxJitter = 25
energy1_ia2 = [x*n for x in [23.13303, 10.1464, 5.97532, 3.36729, 2.49404]]
energy2_ia2 = [x*n for x in [22.15613, 9.68022, 5.84927, 3.28747, 2.45803]]
latency1_ia2 = [133.42847, 132.76107, 133.06927, 132.53167, 133.348]
latency2_ia2 = [156.40655, 156.1754, 153.32793, 155.767, 156.94473]
pdr1_ia2 = [99.672, 99.816, 99.888, 99.92, 99.936]
pdr2_ia2 = [98.742, 98.827, 98.921, 99.222, 99.436]

# CtsMaxJitter = 50
energy1_ia2 = [x*n for x in [x, x, x, x, x]]
energy2_ia2 = [x*n for x in [x, x, x, x, x]]
latency1_ia2 = [x, x, x, x, x]
latency2_ia2 = [x, x, x, x, x]
pdr1_ia2 = [x, x, x, x, x]
pdr2_ia2 = [x, x, x, x, x]

# CtsMaxJitter = 150
energy1_ia2 = [x*n for x in [46.50696, 19.35816, 10.64106, 5.24393, 3.47043]]
energy2_ia2 = [x*n for x in [42.88618, 17.87113, 9.96739, 4.956, 3.29846]]
latency1_ia2 = [544.1742, 546.6681, 548.0082, 544.3568, 548.06015]
latency2_ia2 = [545.6941, 542.74, 544.1245, 542.7127, 541.0689]
pdr1_ia2 = [99.641, 99.821, 100, 100, 100]
pdr2_ia2 = [99.575, 99.589, 99.652, 99.783, 99.827]

base_protocol = [i_energy1, latency1, pdr1, overhead1]
variant_protocol = [i_energy2, latency2, pdr2, overhead2]

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
plt.savefig('../assets/' + filename)
plt.close()
