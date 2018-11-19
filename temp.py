
"""
Created By:
Author: Simranjeet
University:University of Regina
Student Id:200412297
"""


import random
import math
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# NOTE: you must manually remove the header data from the simranjeet.dat
#       prior to attempting to read the data in.


data = pd.read_csv("simranjeet.dat", header=None, delimiter=r"\s+")

x = data[0]
y = data[1]
#Making two list to store time and amplitude
list_time = []
list_amplitude = []
#amplification factor
modulation=2.5

#setting sampling frequency
fs=44100

#populate the lists with the contents of the columns read  
for i in range(0,int(len(x))):
   list_time.append(float(x.iloc[i]))
   list_amplitude.append(float(y.iloc[i]))   

#open a file for writing the contents after distortion effect takes place
f = open("out.dat", "w")

#assign threshold for the purpose of hard clipping distortion
threshold_limit=0.3

#IMPORTANT:performing hard_clipping distortion effect  on input signal
for i in range(0,int(len(y))):
    if(list_amplitude[i]>threshold_limit):
        list_amplitude[i]=threshold_limit
    elif(list_amplitude[i]<-threshold_limit):
        list_amplitude[i]=-threshold_limit
    
#amplification of the signal in order to compare the result 
for i in range(0,int(len(y))):
    list_amplitude[i]=list_amplitude[i]*modulation
    
#plotting the input signal    
plt.ylabel('amplitude')
plt.xlabel('time')
plt.plot(list_time,y)
plt.axis([0,0.05000,-1.00,1.00])
plt.show()


#plotting the output signal after hard clipping distortion
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(list_time,list_amplitude)
plt.axis([0,0.05000,-1.00,1.00])
plt.show()

#write into file
f.write("; Sample Rate "+"44100"+"\n")
f.write("; Channels 1"+"\n"+"\n")

# simple inverse filter
# this should really be done in its own method!
for i in range(0,int(len(list_time))):
   f.write(str(list_time[i])+"   "+str(((list_amplitude[i])))+"\n")  
   

#close the file
f.close()

"""
REFERENCES:
TREVOR TOMESH, PROFESSOR,UNIVERSITY OF REGINA
"""
