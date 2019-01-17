import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
plt.plot(x, FTO.loc[:,'Squat'], color='blue', label='5 Sq') # Squat
plt.plot(x, FTO.loc[:,'Bench'], color='red', label='5 Be') # Bench
plt.plot(x, FTO.loc[:,'Deadlift'], color='green', label='5 DL') # Deadlift

# Plot 3 wave data
plt.plot(x, FTO.loc[:, 'Squat.1'], color='cyan', label='3 Sq') # Squat
plt.plot(x, FTO.loc[:, 'Bench.1'], color='salmon', label='3 Be') # Bench
plt.plot(x, FTO.loc[:, 'Deadlift.1'], color='lime', label='3 DL') # Deadlift

# Plot 531 wave
plt.plot(x, FTO.loc[:, 'Squat.2'], color='darkblue', label='Max Sq') # Squat
plt.plot(x, FTO.loc[:, 'Bench.2'], color='crimson', label='Max Be') # Bench
plt.plot(x, FTO.loc[:, 'Deadlift.2'], color='darkgreen', label='Max DL') # Deadlift

# Legend
plt.legend(
    ['Sq', 'Be', 'DL', '3 Sq', '3 Be', '3 DL','Max Sq', 'Max Be', 'Max DL'], 
    loc='lower right', prop={'size': 7.5}
    )
# Show Plot
# plt.show()

plt.savefig('2018plot.png')