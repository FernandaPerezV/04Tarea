from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

condicion_inicial = [10, 0, 0, 0.4]
p = Planeta(condicion_inicial, 10**(-2.232))#RUT=18.769.232-6
#p = Planeta(condicion_inicial)

N_steps = 245*np.int(1e3)
dt=24500./N_steps
t=np.linspace(0,24500,N_steps)
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

ax1 = fig.add_subplot(211)
plt.suptitle('Trayectoria y energia vs tiempo con $v_{y}(t=0)=0.4$ y  ' r'$\alpha=10^{-2.232}$')
fig.subplots_adjust(hspace=.3)
ax1.plot(x,y)
ax1.grid(True)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2 = fig.add_subplot(212)
ax2.plot(t,energia)
ax2.grid(True)
ax2.set_xlabel('tiempo')
ax2.set_ylabel('energia')


distancia=np.zeros(len(x))
for i in range(len(x)):
    distancia[i]=np.sqrt(x[i]**2+y[i]**2)

vuelta=len(x)/31

x_max=np.zeros(31)
y_max=np.zeros(31)
x_min=np.zeros(31)
y_min=np.zeros(31)
theta_afelio=np.zeros(31)
delta_theta=np.zeros(30)
tiempo=np.zeros(31)
delta_tiempo=np.zeros(30)
velocidad_angular=np.zeros(30)

for i in range(31):
    rango=distancia[i*vuelta:(i+1)*vuelta]
    x_max[i]=x[np.where(rango==rango.max())[0]+i*vuelta]
    y_max[i]=y[np.where(rango==rango.max())[0]+i*vuelta]
    x_min[i]=x[np.where(rango==rango.min())[0]+i*vuelta]
    y_min[i]=y[np.where(rango==rango.min())[0]+i*vuelta]
    theta_afelio[i]=np.arctan(y_max[i]/(float)(x_max[i]))
    tiempo[i]=dt*(np.where(rango==rango.max())[0]+i*vuelta)

for i in range(30):
    delta_theta[i]=theta_afelio[i+1]-theta_afelio[i]
    delta_tiempo[i]=tiempo[i+1]-tiempo[i]
    velocidad_angular[i]=delta_theta[i]/(float)(delta_tiempo[i])

suma_velocidades_angular=0
for velocidad in velocidad_angular:
    suma_velocidades_angular+=velocidad

velocidad_angular_promedio=suma_velocidades_angular/30.

print velocidad_angular_promedio



plt.draw()
plt.show()
plt.savefig('alpha_distinto_de_cero.png')
