import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from matplotlib import pylab
from scipy import stats

# Import csv data
FTO=pd.read_csv('/Users/cgodine/Desktop/gapp/fivemaxest.csv')

# Set axes labels, Plot Data
x=np.arange(10)
plt.xlim([0,10])
plt.ylim([100, 700])
plt.xlabel('Cycle')
plt.ylabel('Pounds')

# Scatter Plots
plt.scatter(x, FTO.iloc[:,1], color='blue') # Squat
plt.scatter(x, FTO.iloc[:,2], color='red') # Bench
plt.scatter(x, FTO.iloc[:,3], color='green') # Deadlift

# Legend
plt.legend(['Squat', 'Bench Press', 'Deadlift'], loc='lower right')

# Linear Regressions
# Squat
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(x, FTO.iloc[:,1])
line1=slope1*x+intercept1
plt.plot(line1)

# Bench
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x, FTO.iloc[:,2])
line2=slope2*x+intercept2
plt.plot(line2)

# Deadlift 
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(x, FTO.iloc[:,3])
line3=slope3*x+intercept3
plt.plot(line3)

# plt.show()

# Save Plot
plt.savefig('2018scatter.png')