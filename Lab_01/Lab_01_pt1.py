# -------------------------------------
# Name: Roberto Sanchez (014587792)
# Date: Sept 16, 2017
# Assignment 1 - Part 1
# -------------------------------------
from random import randint
from numpy import histogram
import matplotlib.pyplot as plt
def sum2dice(N):
    record = []
    # Generates value for each die
    for x in range (0,N):
        sum1 = 0
        counter = 0
        while (sum1 != 7):
            counter += 1
            d1=randint(1,6)
            d2=randint(1,6)
            sum1=d1+d2
            record.append(counter)
    b=range(1,30)
    h1, bin_edges = histogram(record,bins=b)
    b1=bin_edges[1:max(record)]
    # Warning undefine name 'close'??? Couldn't run
    #close('all')
    # Begin generating Plot
    fig1=plt.figure(1)
    plt.stem(b1,h1)
    plt.title('Stem plot - Counter vs occurences')
    plt.xlabel('Counter')
    plt.ylabel('Number of occurrences')
    fig1.savefig('1 EE381 Proj Stoch Exper-1.jpg')
    # Second Figure
    fig2=plt.figure(2)
    p1=h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Probability mass function')
    plt.xlabel('Counter')
    plt.ylabel('Probability')
    fig2.savefig('1 EE381 Proj Stoch Exper-1.jpg')

sum2dice(100000)
