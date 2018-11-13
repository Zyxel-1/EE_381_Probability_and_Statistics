# --------------------------------
# Name: Roberto Sanchez
# Date: October 14, 2017
# Assignment 03 - Part 2
# --------------------------------
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
def CalcBinomial(rounds):
    calc = []
    probability = 1/216.
    #does the binomial calculation
    for x in range(0,17):
        c = sp.misc.comb(rounds,x)
        p = np.power(probability, x)
        q = np.power(1-probability, rounds-x)
        for i in range((int)(c * p * q * rounds)):
            calc.append(x)
#This prints out graph
    b = range(-1,17)
    h1, bin_edges = np.histogram(calc, b)
    b1 = bin_edges[0:17]

    plt.stem(b1, h1/rounds)
    plt.title("Probability Mass Function")
    plt.ylabel("Probability of success")
    plt.xlabel("Number of successes in n=1000 trials")

CalcBinomial(1000)
