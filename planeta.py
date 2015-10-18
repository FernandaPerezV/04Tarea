#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha
        #yo lo agregue
        G=1
        M=1
        m=1
        x0, y0, vx0, vy0=self.y_actual
        r=(x0**2+y0**2)**(0.5)
        self.energia_actual = 0.5*m*(vx0**2+vy0**2)-G*M*m/r + alpha*G*M*m/r**2


    def ec_de_mov(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual
        # fx = ...
        # fy = ...

        #yo hice esto
        G=1
        M=1
        alpha=0
        r=(x**2+y**2)**(0.5)
        fx= -x*( G*M/r**3 - 2*alpha*G*M/r**4)
        fy= -y*( G*M/r**3 - 2*alpha*G*M/r**4)

        return [vx, vy, fx, fy]

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''

        vx,vy,fx,fy=self.ec_de_mov()
        x_new=vx*dt+self.y_actual[0]
        y_new=vy*dt+self.y_actual[1]
        vx_new=fx*dt+self.y_actual[2]
        vy_new=fy*dt+self.y_actual[3]
        condicion_actual=[x_new,y_new,vx_new,vy_new]
        self.y_actual=condicion_actual

        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        #guardamos las condiciones iniciales
        x0,y0,vx0,vy0=self.y_actual

        #cada vez que se calcula un Ki, se recalcula y_actual para calcular Ki+1
        k1=[self.ec_de_mov()[0],self.ec_de_mov()[1],self.ec_de_mov()[2],self.ec_de_mov()[3]]
        self.y_actual=[x0+k1[0]/2. , y0+k1[1]/2. , vx0+k1[2]/2., vy0+k1[3]/2.]

        k2=[self.ec_de_mov()[0],self.ec_de_mov()[1],self.ec_de_mov()[2],self.ec_de_mov()[3]]
        self.y_actual=[x0+k2[0]/2. , y0+k2[1]/2. , vx0+k2[2]/2., vy0+k2[3]/2.]

        k3=[self.ec_de_mov()[0],self.ec_de_mov()[1],self.ec_de_mov()[2],self.ec_de_mov()[3]]
        self.y_actual=[x0+k3[0] , y0+k3[1] , vx0+k3[2], vy0+k3[3]]

        k4=[self.ec_de_mov()[0],self.ec_de_mov()[1],self.ec_de_mov()[2],self.ec_de_mov()[3]]

        x_new=x0+(1/6.)*dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        y_new=y0+(1/6.)*dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        vx_new=vx0+(1/6.)*dt*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
        vy_new=vy0+(1/6.)*dt*(k1[3]+2*k2[3]+2*k3[3]+k4[3])

        #se actualiza y_actual a partir de las condiciones iniciales dando un paso dt
        self.y_actual=[x_new,y_new,vx_new,vy_new]

        pass


    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        #Como Verlet necesita dos puntos anteriores y solo tenemos uno (condiciones iniciales)
        #calcularemos el segundo punto con otro metodo y luego seguiremos con Verlet.
        x0,y0,vx0,vy0=self.y_actual
        vx0,vy0,fx0,fy0= self.ec_de_mov()

        x_new=x0+dt*vx0+fx0*(dt**2)/2.
        y_new=y0+dt*vy0+fy0*(dt**2)/2.

        #Verlet como tal no calcula la velocidad, pero es posible implementarla:
        self.y_actual=[x_new,y_new, vx0, vy0] #solo importa x_new, y_new para calculas los f
        vx1,vy1,fx1,fy1= self.ec_de_mov()

        #vx_new=vx0+fx1*dt/2.
        #vy_new=vy0+fy1*dt/2.
        vx_new=vx0+fx1*dt/2.+fx0*dt/2.
        vy_new=vy0+fy1*dt/2.+fy0*dt/2.

        #finalmente:
        self.y_actual=[x_new, y_new, vx_new, vy_new]
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        G=1
        M=1
        alpha=0
        m=1
        x, y, vx, vy = self.y_actual
        vx,vy,fx,fy= self.ec_de_mov()
        r=(x**2+y**2)**(0.5)

        self.energia_actual=0.5*m*(vx**2+vy**2)-G*M*m/r + alpha*G*M*m/r**2

        pass
