# --------------------------------------
# Name: Roberto Sanchez
# Date: Oct 30, 2017
# Assignment 4 - Central Limit Theorem
# Part 3: Distribution of the Sum of RVs
# --------------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
def DisSumRV(rounds, n):
    # Declaring Variables given in Assignment
    beta = 45
    mu_c = beta * n
    sigma_c = beta * math.sqrt(n)
    Booklist = np.zeros((rounds))
    # Creating Booklist and filling it with random ints
    for i in range(rounds):
        for j in range(n):
            temp = np.random.exponential(beta)
            Booklist[i] = Booklist[i] + temp
    # Begins plotting curve
    fig1 = plt.figure(n+1)
    bins = [float(Booklist) for Booklist in np.linspace(350,2000,50)]
    h1, bin_edges = np.histogram(Booklist,bins,density=True)
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]
    plt.bar(b1,h1,width=barwidth, edgecolor='w')
    g = np.linspace(350,2000)
    fact = 1/(np.sqrt(2*np.pi*sigma_c * sigma_c))
    y = fact* np.exp(-(g-mu_c)**2/(2*sigma_c*sigma_c))
    # Plotting
    plt.plot(g,y,color='red')
    plt.title('CDF of the lifetime of a carton')
    plt.xlabel('Lifetime')
    plt.ylabel('CDF')
    H1 = np.cumsum(h1)*barwidth
    plt.bar(b1,H1,width=barwidth,edgecolor='w')
    fig1.show()
DisSumRV(10000,24)
