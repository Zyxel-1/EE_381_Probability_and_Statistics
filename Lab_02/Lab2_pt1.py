# ------------------------------------
# Name: Roberto Sanchez
# Date: October 3, 2017
# Assignment 02 - Conditional Probabilities
# Part 1
# ------------------------------------
import random
E0 = 0.02
E1 = 0.03
P0 = 0.4
def transmittedMsg(S):
    T= random.uniform(0,1)
    if T<=E0 and S==0:
        return 1
    elif T > E0 and S==0:
        return 0
    elif T> E1 and S == 1:
        return 1
    elif T <=E1 and S == 1:
        return 0
counter = 0
S= 0

for x in range (100000):
    M = random.uniform(0,1)
    if M <= P0:
        S = 0
    elif M > P0:
        S = 1
    R = transmittedMsg(S)
    if S == R:
        counter = counter + 1
print("Probability of Transmission failure is :", (1-(counter/100000)))
