import numpy as np
import matplotlib.pyplot as plt
import designingModel as md
#FTCS: to solve partial differential equations 
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


#For FTCS:
N=100 # resolution of rod
dx = 1/(N+1)
r = 0.2
steps = 10
x = np.linspace(0, 1, N+2)

sinMode = 6
u = np.sin(sinMode*np.pi*x)

#Expectation derived from diffusion Eq
xi = 1 - 4 * r * np.sin(sinMode * np.pi * dx / 2) ** 2
expected = xi**steps * u
actualTemp = tempSolver(u, r, steps)

#Exact solution:
length = 1.0
alpha = 1.0
dx = length/(N+1)
dt = r*dx**2 / alpha
endTime = steps * dt
exactSolution = (np.exp(-alpha * (sinMode * np.pi / length)**2* endTime)*np.sin(sinMode*np.pi* x/length))


print("Difference between FTCS and exact solution for partial equation: " + np.max(np.abs(actualTemp-exactSolution))) # difference
plt.plot(expected)
plt.plot(actualTemp)
plt.plot(exactSolution)
plt.show()

