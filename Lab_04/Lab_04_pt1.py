# --------------------------------------
# Name: Roberto Sanchez
# Date: Oct 30, 2017
# Assignment 4 - Central Limit Theorem
# Part 1: The Central Limit Theorem
# --------------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
def CLT(rounds,books):
    # Declaring variables given in Assignment
    mu_w = 2
    sigma_w = 0.57
    sigma_sn = sigma_w * math.sqrt(books)
    var = sigma_sn * sigma_sn
    mu_sn = books * mu_w
    # Creating list full of zeros
    Booklist = np.zeros((rounds))
    # Creating Booklist and filling it with random ints
    x = books * 1
    y = books * 3
    for i in range(rounds):
        for j in range(books):
            temp = np.random.uniform(w,y)
            Booklist[i] = Booklist[i] + temp
        Booklist[i] = Booklist[i] * 1/books
    print(Booklist)
    # Begin plotting curves
    fig1 = plt.figure(books + 1)
    bins = [float(Booklist) for Booklist in np.linspace(x,y,30)]
    h1, bin_edges = np.histogram(Booklist,bins,density=True)
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]
    plt.bar(b1,h1,width = barwidth, edgecolor='w')
    # Creating Gaussian Curve
    x0 = np.linspace(books * 1, books* 3)
    fact = 1 / (np.sqrt(2*np.pi*var))
    y = fact*np.exp(-(x0-mu_sn)**2 / (2*var))
    # Plotting
    plt.plot(x0,y,color='red')
    plt.title('PDF of books height for n=' + str(books)+' books.')
    plt.xlabel('Books height for n=' + str(books) +' books.')
    plt.ylabel('PDF')
    fig1.show()
CTL(10000,1)
