# --------------------------------
# Name: Roberto Sanchez
# Date: October 14, 2017
# Assignment 03 - Part 3
# --------------------------------
import numpy as np
import matplotlib.pyplot as plt
def CalcPoisson(rounds):
    probability = 1/216
    lamda = probability * rounds
    PoissonNum = []
    e = 2.718281

    for x in range (17):
        lamda2 = np.power(lamda,x)
        e2 = np.power(e,lamda)
        factorial = np.math.factorial(x)
        Poisson = (int)(lamda2*rounds/factorial*e2)
        for i in range(Poisson):
            PoissonNum.append(x)
    #This prints the graph
    b = range(-1,16)
    h1, bin_edges = np.histogram(PoissonNum, bins = b)
    b1 = bin_edges[0:16]

    #plot
    plt.stem(b1, h1/rounds)
    plt.title("Probability Mass Function")
    plt.ylabel("Probability of success")
    plt.xlabel("Number of successes in n = 1000 trials")

    #show graph
    plt.show()
CalcPoisson(1000)
