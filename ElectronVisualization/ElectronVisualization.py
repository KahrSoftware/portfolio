from math import *
from vpython import *
import random as random
from numpy import *

print('Calculating...')

# Probability density functions for different quantum numbers
def psi100(r):
    return(1/sqrt(pi*a**3))*exp(-r/a)

def psi210(r,t):
    return(1/sqrt(32*pi*a**3))*(r/a)*exp(-r/(2*a))*cos(t)

def psi211(r,t,p):
    return(-1/sqrt(64*pi*a**3))*(r/a)*exp(-r/(2*a))*sin(t)*exp(-1j*p)

def psi21m(r,t,p):
    return(1/sqrt(64*pi*a**3))*(r/a)*exp(-r/(2*a))*sin(t)*exp(-1j*p)

def psi2p(r,t,p):
    return(1/sqrt(32*pi*a**3))*(r/a)*exp(-r/(2*a))*sin(t)*cos(p)

# Canvas, axes and, labels
canvas(forward=vec(-1,-1,-1),up=vec(0,0,1))

xyplane = box(pos = vector(0,0,0), length = 10., width=10., height = 0.1, color = color.white, 
              opacity=0.25)
yzplane = box(pos = vector(0,0,0), length = 0.1, width=10., height = 10, color = color.white, 
              opacity = 0.25)
xzplane = box(pos=vector(0,0,0), length = 10.,width = 0.1, height = 10, color = color.white, 
              opacity=0.25)

label(pos=vec(6,0,0), text='x')
label(pos=vec(0,6,0), text='y')
label(pos=vec(0,0,6), text='z')

# Scale factor
a = 1

# Loop through points in a 10 x 10 x 10 cube
points = []
for x in arange(-10.0,10.0,0.1):
    for y in arange(-10.0,10.0,0.1):
        for z in arange(-10.0,10.0,0.1):
            
            # Change to spherical coordinates
            r = sqrt(x**2+y**2+z**2)
            t = atan2(y,x)
            p = acos(z/r)

            # Get the probability density function, psi squared

            prob = psi100(r)**2
            #prob = psi210(r,t)**2
            #prob = psi211(r,t,p)**2
            #prob = psi21m(r,t,p)**2
            #prob = psi2p(r,t,p)**2
            
            # Perform an experiment at each point, using a random spread to show the distribution
            rand = random.random()
            if rand <= prob:
                points.append([x,y,z])

# Draw a red sphere for the proton
sphere(pos=vector(0,0,0), radius=0.2, color=color.red)
# Draw a blue sphere for each electron position
for i in points:
    sphere(pos=vector(i[0],i[1],i[2]), radius=0.1, color=color.blue)
print("Done")