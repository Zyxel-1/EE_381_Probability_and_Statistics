# ------------------------------------
# Name: Roberto Sanchez
# Date: October 3, 2017
# Assignment 02 - Conditional Probabilities
# Part 3
# ------------------------------------
import random
E1 = 0.03
E0 = 0.02
P0 = 0.4
#In transmission
def transmittedMsg(S):
    T= random.uniform(0,1)
    if T<=E0 and S==0:
        return 1
    elif T> E1 and S == 1:
        return 1


#Runs the message one bit at a time (100000) and records success or failure
counter = 0
S = 1
for x in range(100000):
# transmittedMsg returns if
    R = transmittedMsg(S)
    if S == R:
        counter = counter + 1
print("P(R=1|S=1", (counter/100000))
