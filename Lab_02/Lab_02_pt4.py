# ------------------------------------
# Name: Roberto Sanchez
# Date: October 3, 2017
# Assignment 02 - Conditional Probabilities
# Part 4
# ------------------------------------
import random
E1 = 0.03
E0 = 0.02
P0 = 0.4
#In transmission
def transmittedMsg(S):
    T= random.uniform(0,1)
    if T <= E0 and S == 0:
        return 1
    elif T > E1 and S == 1:
        return 1
    else :
        return 0
def checkmajority(R):
    z = 0
    for i in R:
        if i == 0:
            z = z+1
    if z > len(R)/2:
        return 0
    else:
        return 1




#Runs the message one bit at a time (100000) and records success or failure
counter = 0
for x in range(100000):
    M = random.uniform(0,1)
    if M <= P0:
        S = 0
    elif M > P0:
        S = 1
    R = [transmittedMsg(S),transmittedMsg(S),transmittedMsg(S)]
    R1 = checkmajority(R)
    if S == R1:
        counter = counter + 1

print("P(R=1|S=1", (1-(counter/100000)))
