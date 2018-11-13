# --------------------------------------
# Name: Roberto Sanchez
# Date: Oct 30, 2017
# Assignment 4 - Central Limit Theorem
# Part 2: Exponentially Distributed RVs.
# --------------------------------------
import numpy as np
import matplotlib.pyplot as plt
def ExpoDisRV(rounds):
    beta = 0.5
    # Exponentially Distributed R.V.
    T = np.zeros((rounds))
    # Create Random ints
    for i in range (rounds):
        T[i] = np.random.exponential(beta)
    # Creating Bins
    bins = [float(T) for T in np.linspace(0,5,31)]
    # Creating Curve
    h1, bin_edges = np.histogram(T,bins,density=True)
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]
    # Create other curve
    plt.bar(b1, h1, width=barwidth,edgecolor='w')
    x = np.linspace(0,5)
    gx = (1 / beta) * np.exp((-1 / beta)*x)
    plt.title('Exponentially Distributed RVs: RV T vs Function g(x)')
    plt.xlabel('X - Values for N=10,000')
    plt.ylabel('PDF')
    plt.show()
ExpoDisRV(10000)
