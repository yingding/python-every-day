"""
This example shows code snippet to make a bar plot with matplotlib.
Customized xticks, space, margin, and DateFormatter

Reference:
https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html#sphx-glr-gallery-ticks-ticklabels-rotation-py

pandas type datetime64 issue in previous matplotlib
https://stackoverflow.com/questions/26526230/plotting-datetimeindex-on-x-axis-with-matplotlib-creates-wrong-ticks-in-pandas-0
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter
from pandas import DatetimeIndex

# dtype='datetime64[ns]'
# https://stackoverflow.com/questions/26526230/plotting-datetimeindex-on-x-axis-with-matplotlib-creates-wrong-ticks-in-pandas-0

# date_index: DatetimeIndex = pd.date_range(start="1/1/2000", periods=200)

series = pd.Series(np.random.randn(200),
    index=pd.date_range(start="1/1/2000", periods=200))

# important to get the ax and fig, to allow xticks rotation and formatting
fig, ax = plt.subplots() 
# convert pandas datetime64 type of DatetimeIndex object to python datetime object
# py_datetime_idx = series.index.to_pydatetime()

# matplotlib 3.6.1 fixed issue of pandas datetime64 type
py_datetime_idx = series.index

# previous matplotlib doesn't work with datetime64 
ax.bar(py_datetime_idx, series.to_numpy()) 

# use the subplot bar chart, to allow xaxis settings
# set the max and min of xticks to match the series index
# ax.set_xlim(py_datetime_idx.to_numpy()[0], py_datetime_idx.to_numpy()[-1]) 
ax.set_xlim(py_datetime_idx[0], py_datetime_idx[-1])

# previous matplotlib, we would need to set the xticks 
# to use python datetime instead of dateime64 from pandas
# ax.set_xticks(series.index.to_pydatetime())
ax.set_xticks(series.index)

# set xtick to be show by every 10 day
ax.xaxis.set_major_locator(DayLocator(interval=10))
# set the xtick datetime format
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d')) 
 
# rotate the xtick 90 degree
# plt.xticks(rotation = 90)
plt.xticks(rotation = "vertical")
# Set the font size of xticks, default is 10
plt.xticks(fontsize=10)

# use margin to controll the axis scale, fraction of firgure height
plt.margins(0.15)

# Tweak spacing to prevent clipping of tick-labels, bottom is a fraction of figure height
# top and bottom adds to 1, and bottom < top
plt.subplots_adjust(top=0.8, bottom=0.2)
plt.show()

# ax = series.plot(kind="bar")

# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
# plt.plot([1,2,3], [10,20,30])
# plt.show()

# print(series.head(3))