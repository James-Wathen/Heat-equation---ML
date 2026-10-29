import matplotlib.pyplot as plt
import numpy as np

L = 1.0 # Length of the rod in meters
N = 100 # Resolution of rod's temperature
a = L/N # length per point
k0 = 1 # Thermal conductivity
c = 1 # Specific heat capacity
p = 1 # Density
k = k0 / (c * p) # Thermal diffusivity
deltaT = 0.01 # Time step

T = np.empty(N+2, float)# this way we have indeces 0 and N+1 for bondary conditions, while N is only points in the rod
newT = np.empty(N+2, float)
#Initial conditions are only applied to T (this being middle temperature)
# But boundary conditions to both T and newT so that they carry through
leftBoundary= 0
rightBoundary = 0
middleT = 100


T[0] = leftBoundary
T[-1] = rightBoundary
T[1:-1] = middleT
newT[0] = leftBoundary
newT[-1] = rightBoundary

def tempUpdate(T, newT):
    const = k * t / (a**2)
    newT[1:-1] = T[1:-1] + const * (T[2:N+1] + T[0:N-1] - 2*T[1:N])
    # I love numpy. This updates newT accoridng to FTCS because T[2:N+1] is on the right of it all, and T[0:N-1] is on the left of it all.
    return T, newT # This return method allows newT and T to be easily swapped and I found it in the linked git hub in the readme

listTime = np.linspace(0, 1000)
finalTime = listTime[-1]
t = 0.0
while t < finalTime:
    newT, T = tempUpdate(T, newT) #updates and swaps
    t+=deltaT

plt.plot(T)
plt.show()
