from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

condicion_inicial = [10, 0, 0, 0.4]
p = Planeta(condicion_inicial)

N_steps = 7*np.int(1e5)
dt=4000./N_steps
t=np.linspace(0,4000,N_steps)
#creamos los arrays en que se guardara la informacion
x= np.zeros(N_steps)
y= np.zeros(N_steps)
vx= np.zeros(N_steps)
vy= np.zeros(N_steps)
energia = np.zeros(N_steps)

x[0]= 10
y[0]= 0

energia[0]=p.energia_actual


for i in range(1, N_steps):
    p.avanza_verlet(dt)
    x[i]=p.y_actual[0]
    y[i]=p.y_actual[1]
    p.energia_total()
    energia[i]=p.energia_actual


fig = plt.figure(1)
fig.clf()

ax1 = fig.add_subplot(211)
ax1.plot(x,y)
ax2 = fig.add_subplot(212)
ax2.plot(t,energia)
#ax2.set_ylim(-1,1)
plt.draw()
plt.show()
plt.savefig('verlet.png')
