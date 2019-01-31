"""
Her kan man kombinere eksperiment med model.

Eksperiment: 
	Slipp en tennisball fra 1 meters høyde
	Film
	Estimer:
		- Hvor høyt når ballen på sitt første sprett?
		- Hvor lang tid tar det før ballen treffer bakken for første gang?
		- Hvor lang tid tar det ca før ballen faller til ro?

	Regn ut for hånd
		- Hvor lang tid bør det ta før ballen treffer bakken (se bortifra luftmotstand)

	Modeller på PC:
		- Bruk Euler's metode til å modellere ballen
		- Juster dempningsfaktoren i sprettet B

	Drøft:
		- Er luftmotstand viktig i dette eksempelet?
"""


from pylab import *

g = 9.81
m = 0.0585

T = 20
dt = 0.01
N = int(T/dt)

y = np.zeros(N+1)
v = np.zeros(N+1)
t = np.zeros(N+1)


y[0] = 1


for i in range(N):
	t[i+1] = t[i] + dt
	v[i+1] = v[i] - m*g*dt
	y[i+1] = y[i] + v[i+1]*dt 

	if y[i+1] < 0:
		v[i+1] = -0.8*v[i+1]
		y[i+1] = -y[i+1]
		

plt.plot(t, y)
plt.xlabel('Tid [sekunder]')
plt.ylabel('Høyde over bakken [meter]')
plt.show()



