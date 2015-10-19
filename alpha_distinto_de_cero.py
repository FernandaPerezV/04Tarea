from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

condicion_inicial = [10, 0, 0, 0.4]
p = Planeta(condicion_inicial, 10**(-2.232))#RUT=18.769.232-6
#p = Planeta(condicion_inicial)

N_steps = np.int(1e6)
dt=25000./N_steps
t=np.linspace(0,25000,N_steps)
#creamos los arrays en que se guardara la informacion
x= np.zeros(N_steps)
y= np.zeros(N_steps)
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

indice=np.where(energia==energia.min())
ax1 = fig.add_subplot(211)
plt.suptitle('Trayectoria y energia vs tiempo con $v_{y}(t=0)=0.4$ y  ' r'$\alpha=10^{-2.232}$')
fig.subplots_adjust(hspace=.3)
ax1.plot(x,y)
ax1.plot(x[indice],y[indice],'o',color='r')
ax1.grid(True)
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2 = fig.add_subplot(212)
ax2.plot(t,energia)
ax2.grid(True)
ax2.set_xlabel('tiempo')
ax2.set_ylabel('energia')
plt.draw()
plt.show()
plt.savefig('alpha_distinto_de_cero.png')
