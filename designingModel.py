import matplotlib.pyplot as plt
import numpy as np

L = 1.0 # Length of the rod in meters
N = 100 # Resolution of rod's temperature
a = L/N # length per point
k0 = 1 # Thermal conductivity
c = 1 # Specific heat capacity
p = 1 # Density
k = 4.23e-6#k0 / (c * p) # Thermal diffusivity
deltaT = 1e-4 # Time step

#preT = np.empty(N+2, float)# this way we have indeces 0 and N+1 for bondary conditions, while N is only points in the rod
#newT = np.empty(N+2, float)
#Initial conditions are only applied to T (this being middle temperature)
# But boundary conditions to both T and newT so that they carry through
leftBoundary= 0
rightBoundary = 0
middleT = 50
# preT[0] = leftBoundary
# preT[-1] = rightBoundary
# preT[1:-1] = middleT
# newT[0] = leftBoundary
# newT[-1] = rightBoundary

const = k * deltaT / (a**2) # diffusivity*time step / length in each point^2 = k dt/dx^2, which is the change in the diffusivity equation

def tempSolver(initialTempFunction, constFTCS, totalSteps):
    preT = np.asarray(initialTempFunction, dtype=float).copy() # ensuring it is a float
    newT = preT.copy()
    const = constFTCS

    def tempUpdate(preT, newT):
        newT[1:-1] = preT[1:-1] + const * (preT[2:] + preT[0:-2] - 2*preT[1:-1])
        # I love numpy. This updates newT accoridng to FTCS because T[2:] is on the right of it all, and T[0:-2] is on the left of it all.
        return preT, newT # This return method allows newT and T to be easily swapped and I found it in the linked git hub in the readme

    step = 0
    while step < totalSteps: # building preT into the final temperature model
        newT, preT = tempUpdate(preT, newT)
        step+=1

    return preT


