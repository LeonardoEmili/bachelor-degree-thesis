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

# Select if plotting simulation with interest dissemination phase (energy only - m_type should be 0)
interest_active = True

# Names and labels
types = ["energy", "latency", "pdr", "overhead"]
labels = ["Energy spent by the network [J]", "Latency [ms]", "Packet delivery ratio [%]", "Packets overhead [%]"]
filename = types[m_type] + '_plot.png'
if interest_active:
	filename = "interest_" + filename

# Raw data to plot (parsed from GC simulations) - CtsMaxJitter = 100
n = 140
energy1 = [x*n for x in [37.73876, 16.07003, 8.88417, 4.47382, 3.13403]]
energy2 = [x*n for x in [33.60001, 14.31184, 8.14755, 4.2216, 2.92407]]
latency1 = [392.87577, 386.10047, 385.0174, 382.8534, 380.6449]
latency2 = [382.4569, 374.9848, 373.6934, 372.6346, 372.6205]
pdr1 = [99.665, 99.833, 99.876, 99.898, 99.96]
pdr2 = [99.512, 99.662, 99.706, 99.766, 99.821]
overhead1 = [22.3, 22.2, 22.6, 22.3, 22.0]
overhead2 = [17.8, 17.8, 18.1, 17.8, 16.5]

# Data from simulation with dissemination active
i_energy1 = [x*n for x in [38.44381, 16.35294, 9.149, 4.56977, 3.08084]]
i_energy2 = [x*n for x in [34.49227, 14.65808, 8.32379, 4.26025, 2.93325]]

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
plt.xlabel('iaTime [ms]', fontsize=12)
plt.xticks([r + barWidth/2 for r in range(len(bars1))],
           ['2', '5', '10', '25', '50'])

plt.gca().set_ylim([0,5600])

plt.locator_params(axis='y', nbins=6)

# Create legend & Show graphic
plt.legend(loc="upper right")
plt.savefig('../assets/' + filename)
plt.close()
