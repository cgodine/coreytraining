import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from matplotlib import pylab
from scipy import stats

# Import csv data
FTO=pd.read_csv('/Users/cgodine/Desktop/gapp/fivethreeone_2018.csv')

# Set axes limits, labels, grid
x=np.arange(10)
plt.xlim([0,10])
plt.ylim([100, 700])
plt.xlabel('Cycle')
plt.ylabel('Pounds')
plt.minorticks_on()
plt.grid(which='major', axis='y', linestyle='-')
plt.grid(which='minor', axis='y', linestyle=':')

# Chart title
plt.title('Corey\'s 2018 5/3/1 Progress')

# Plot data for 5 wave
plt.scatter(x, FTO.loc[:,'Squat'], color='blue', label='5 Sq') # Squat
plt.scatter(x, FTO.loc[:,'Bench'], color='red', label='5 Be') # Bench
plt.scatter(x, FTO.loc[:,'Deadlift'], color='green', label='5 DL') # Deadlift

# Plot 3 wave data
plt.scatter(x, FTO.loc[:, 'Squat.1'], color='cyan', label='3 Sq') # Squat
plt.scatter(x, FTO.loc[:, 'Bench.1'], color='salmon', label='3 Be') # Bench
plt.scatter(x, FTO.loc[:, 'Deadlift.1'], color='lime', label='3 DL') # Deadlift

# Plot 531 wave
plt.scatter(x, FTO.loc[:, 'Squat.2'], color='darkblue', label='Max Sq') # Squat
plt.scatter(x, FTO.loc[:, 'Bench.2'], color='crimson', label='Max Be') # Bench
plt.scatter(x, FTO.loc[:, 'Deadlift.2'], color='darkgreen', label='Max DL') # Deadlift

# Legend
plt.legend(
    ['Sq', 'Be', 'DL', '3 Sq', '3 Be', '3 DL','Max Sq', 'Max Be', 'Max DL'], 
    loc='lower right', prop={'size': 7.5}
    )

"""# Linear Regressions
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
plt.plot(line3)"""

# plt.show()

# Save Plot
plt.savefig('2018scatter.png')