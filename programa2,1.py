# lineplot.py
import numpy as np
impor pylb as pl
# Make an array of x values
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
# Make an array of y values for each x value
y = [0,2,2,3,5,4,5,5,5,4,4,4,4,3,2,5,6,3,2,4,2,2]
# use pylab to plot x and y
pl.plot(x, y)
# show the plot on the screen
pl.savefig('templ.png')
