# --------------------------------------------
# Name: Roberto Sanchez (014587792)
# Date: Sept 16, 2017
# Assignment 1 - Part 4
# --------------------------------------------
from random import randint
def comparePasswords(ps):
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for x in range (0,100000):
        if ps == characters[randint(0,25)] + characters[randint(0,25)] + characters[randint(0,25)] + characters[randint(0,25)]:
            return 1
    return 0
def experiment(N):
    #Creates List of passwords
    ps = 'aaaa'
    # Checking Experiment
    result = 0
    for x in range(0,N):
        print(x)
        result += comparePasswords(ps)
    print("Result = ",result)
    print("The probablity of that at least one of the words in the hacker's list will match your password is  ",result/N)

experiment(1000)
'''
OUTPUT:
// Below ran at 10^5
The probablity of that at least one of the words in the hacker's list of size 10^5 will match your password is   0.22
The probablity of that at least one of the words in the hacker's list of size 10^5 will match your password is   0.175
The probablity of that at least one of the words in the hacker's list of size 10^5 will match your password is   0.189
The probablity of that at least one of the words in the hacker's list of size 10^5 will match your password is   0.211
// 700000
The probablity of that at least one of the words in the hacker's list will match your password is   0.796
// 600000
The probablity of that at least one of the words in the hacker's list will match your password is   0.731
// 200000
The probablity of that at least one of the words in the hacker's list will match your password is   0.334
// 315000
The probablity of that at least one of the words in the hacker's list will match your password is   0.482
'''
