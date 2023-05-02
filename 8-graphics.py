from matplotlib import pyplot as plt
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

with open('settings.txt') as file:
    settings=[float(i) for i in file.read().split('\n')]

print(settings)
data=numpy.loadtxt('data.txt', dtype=int) * settings[1]

data_time = numpy.array([i * 0.041 for i in range(data.size)])

fig, ax=plt.subplots(figsize=(16, 10), dpi=500)

#ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.set_title("\n".join(wrap('Charge and Discarge of RC', 60)), loc = 'center')

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.set_ylabel("V, vlt")
ax.set_xlabel("t, s")

ax.text(5, 0.5, 'time of charge: {0:.4}'.format(data_time[data.argmax()]), fontsize = 20)
ax.text(5, 0.75, 'time of discharge: {0:.4}'.format(data_time[-1] - data_time[data.argmax()]), fontsize = 20)

ax.plot(data_time, data, c='black', linewidth=1)
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'red', s=50, label ='v(t)')

ax.legend(shadow = False, loc = 'right', fontsize = 20)

fig.savefig('graph.png')
fig.savefig('graph.svg')
