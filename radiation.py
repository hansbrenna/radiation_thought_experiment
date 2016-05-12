from __future__ import print_function
import sys
import numpy as np
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
import seaborn as sns

"""Back radiation thought experiment illustrative simulation"""

sb = 5.67e-8 #Stephan-Boltzmann constant
S = 100 #Constant energy input term
c = 3e8 #speed of light
N = 100
dz = N*c #Distance between plates (n light seconds)
dt = 1 #time step, seconds
cap = 10 #heat capacity

eii = 0.5
Ti0 = 0 #K
Tii0 = 0 #K
z = np.linspace(0,dz,N/dt) #Discretized space
n = z.shape[0]

jiz = np.zeros(z.shape)
jiiz = np.zeros(z.shape)

t0 = 0
ts = 30*N
time = np.arange(t0,ts,dt)

ji = np.zeros(time.shape)
jii = np.zeros(time.shape)
Ti = np.zeros(time.shape)
Tii = np.zeros(time.shape)
Su = np.zeros(time.shape)
dTi = 0
dTii = 0

for i in xrange(1,int(ts)):
    if i == ts/2:
        eii = 0.8
    dTi =1.0/cap*(S+jiiz[0]-ji[i-1])*dt
    #print(dTii)
    Ti[i] = Ti[i-1]+dTi
    ji[i] = sb*Ti[i]**4
    jiz[1:]=jiz[0:n-1]
    jiz[0] = ji[i]
    dTii =1.0/cap*(eii*jiz[n-1]-2*jii[i-1])*dt
    Tii[i] = Tii[i-1]+dTii
    jii[i] = eii*sb*Tii[i]**4
    jiiz[0:n-1]=jiiz[1:n]
    jiiz[n-1] = jii[i]
    Su[i] = (1-eii)*jiz[n-1]+jii[i]

fig1 = plt.figure()
plt.plot(time,Ti,time,Tii)

fig1.savefig('temperatures.png')

fig2 = plt.figure()
plt.plot(time,Su)
fig2.savefig('rad_TOA.png')





