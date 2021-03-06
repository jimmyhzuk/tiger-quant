import os

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook


"""
如何安装样本数据：
conda config --add channels conda-forge
#Once the conda-forge channel has been enabled, matplotlib, matplotlib-base, mpl_sample_data can be installed with:

conda install matplotlib matplotlib-base mpl_sample_data
#It is possible to list all of the versions of matplotlib available on your platform with:

conda search matplotlib --channel conda-forge
"""

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
with open(os.path.join(matplotlib._get_data_path(), 'sample_data/goog.npz'), mode='rb') as datafile:
    r = np.load(datafile)['price_data'].view(np.recarray)

with open(os.path.join(matplotlib._get_data_path(), 'sample_data/aapl.npz'), mode='rb') as datafile:
    r2 = np.load(datafile)['price_data'].view(np.recarray)

fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
ax.plot(r2.date, r2.adj_close)

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

# round to nearest years...
datemin = np.datetime64(r.date[0], 'Y')
datemax = np.datetime64(r.date[-1], 'Y') + np.timedelta64(1, 'Y')
ax.set_xlim(datemin, datemax)


# format the coords message box
def price(x):
    return '$%1.2f' % x


ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = price
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

plt.show()
