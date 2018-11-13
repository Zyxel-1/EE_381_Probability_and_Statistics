# --------------------------------
# Name: Roberto Sanchez
# Date: October 14, 2017
# Assignment 03 - Part 1
# --------------------------------
import numpy as np
import random
import matplotlib.pyplot as plt
# Number of rounds ie: number of expiremnets run in this case 10,000
def Experiment(rounds):
    #Tracks all the success per trial
    ListOfSuccesses = []
    # run experiment in number of rounds
    for y in range(rounds):
         #runs one trial, tosses 3 dices and see if its 3 sixes
        TrialSuccessful = 0
        # This is for one trial, repeated 1000 times
        for x in range(1000):
             #tracks if we have a six in a row when tossing 3 dies
             GotaSix = 0
             #Tossing 3 Dies
             for z in range(3):
                 # Is the value 6?
                 if random.randint(1,7) == 6:
                     #track it
                     GotaSix += 1
             #After tossing 3 dies, did we get 3 sixes?
             if GotaSix == 3:
                 #Track it
                 TrialSuccessful += 1;
         #AFter one trial, store value in listS
        ListOfSuccesses.append(TrialSuccessful)
        #print("Success in Trial ",y,": ",TrialSuccessful)
    # This prints out the graph
    b = range(-1,17)
    h1, bin_edges = np.histogram(ListOfSuccesses, bins = b)
    b1 = bin_edges[0:17]
    # stem(x,y) cordinates
    plt.stem(b1, h1/rounds)
    plt.title("Probability Mass Function")
    plt.ylabel("Probability of success")
    plt.xlabel("Number of successes in n=1000 trials")

Experiment(10000)
