from matplotlib import pylab
import numpy as np

def loadFile():
	inFile = open('julyTemps.txt')
	high_temps = []
	low_temps = []
	for line in inFile:
		fields = line.split()
		if len(fields) < 3 or not fields[0].isdigit():
			continue 
		else:
			high_temps.append(int(fields[1]))
			low_temps.append(int(fields[2]))
	return (low_temps, high_temps)

	
def producePlot(lowTemps, highTemps):
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    
        
(low_temps, high_temps) = loadFile()    
producePlot(low_temps, high_temps)
        

              

	
"""
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot([1,2,3,4], [1,7,3,5])
plt.show()
"""