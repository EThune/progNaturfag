"""
I dette programmet skal vi modellere en
forbrenningsreaksjonen hvor hydrogengass brennes.

Den kjemiske formelen er 
	2H2 + O2 -> 2H2O 
"""

from pylab import *

dt = 0.01
T = 10

N = int(T/dt)
t = zeros(N+1)
H2 = zeros(N+1)
O2 = zeros(N+1)
H2O = zeros(N+1)

k = 1

H2[0] = 2
O2[0] = 1

for i in range(N):
	t[i+1] = t[i] + dt
	H2[i+1] = H2[i] - 2*k*H2[i]**2*O2[i]*dt
	O2[i+1] = O2[i] - k*H2[i]**2*O2[i]*dt
	H2O[i+1] = H2O[i] + k*H2[i]**2*O2[i]*dt


plot(t, H2)
plot(t, O2)
plot(t, H2O)
legend(('H2', 'O2', 'H2O'))
xlabel('Tid')
ylabel('Konsentrasjon [M]')
show()