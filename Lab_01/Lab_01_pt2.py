# ------------------------------------------------
# Name: Roberto Sanchez
# Date: Sept. 16, 2017
# Assignment 01 - Part 2
# ------------------------------------------------
from random import randint
def coin2(N):
    coins = []
    for x in range(0,N):
        #Let 0 be tails and 1 be heads
        coin = randint(0,1)
        coins.append(coin)
    #print ("List of Coin Values = ",coins)
    heads = sum(coins)

    if heads == 50:
        #print ("This experiment was a success!")
        return 1
    else:
        #print ("This experiment was a failure...")
        return 0
def experiment(N):
    result = []
    for x in range(0,N):
        res = coin2(100)
        result.append(res)
   # print("list", result)
    prob = sum(result)/N
    print("Probability of getting 50 heads when tossing 100 coins 100,000 times are ",prob)

experiment(100000)
'''
OUTPUT:
runfile('/home/beryl/test.py', wdir='/home/beryl')
Probability of getting 50 heads when tossing 100 coins 100,000 times are  0.08024

runfile('/home/beryl/test.py', wdir='/home/beryl')
Probability of getting 50 heads when tossing 100 coins 100,000 times are  0.07996

runfile('/home/beryl/test.py', wdir='/home/beryl')
Probability of getting 50 heads when tossing 100 coins 100,000 times are  0.07886

'''
