import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import csv data
FTO=pd.read_csv('/Users/cgodine/Desktop/gapp/fivemaxest.csv')

# Set axes labels, Plot Data
x=np.arange(10)
plt.xlim([0,10])
plt.ylim([100, 700])
plt.xlabel('Cycle')
plt.ylabel('Pounds')


plt.plot(x, FTO.iloc[:,1], color='blue') # Squat
plt.plot(x, FTO.iloc[:,2], color='red') # Bench
plt.plot(x, FTO.iloc[:,3], color='green') # Deadlift

# Legend
plt.legend(['Squat', 'Bench Press', 'Deadlift'], loc='lower right')
# Show Plot
plt.savefig('2018.png')