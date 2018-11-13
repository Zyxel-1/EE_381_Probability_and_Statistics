# -------------------------------
# Name: Roberto Sanchez
# Date: November 12, 2017
# Assignment 05 - Confidence Intervals
# Part 2 - Using the sample mean to estimate the population mean
# -------------------------------
import numpy as np
import matplotlib.pyplot as plt

def ConfInterval(n):
    # Given values from handout
    NumBaring = 1000000
    mean = 75
    stddev = 7.5
    successes_n95 = 0
    successes_t95 = 0
    successes_n99 = 0
    successes_t99 = 0
    M = 10000
    # Calculate Normal
    bearings = np.random.normal(mean,stddev,NumBaring)
    for j in range(M):
        sample = np.random.choice(bearings,n)
        mean_s = sum(sample)/n
        stddev_s = 0
        for i in range(len(sample)):
            stddev_s = stddev_s + ((sample[i]-mean_s)**2)
        stddev_s = (stddev_s/(n-1))**(1/2)
        z_95 = 1.96
        z_99 = 2.58
        # Finding upper and lower limits
        lowerLimit_n95 = mean_s-z_95*stddev_s/(n**0.5)
        upperLimit_n95 = mean_s+z_95*stddev_s/(n**0.5)

        lowerLimit_n99 = mean_s-z_99*stddev_s/(n**0.5)
        upperLimit_n99 = mean_s+z_99*stddev_s/(n**0.5)
        # Giving t values based on metrics
        if n == 5:
            t_95 = 2.78
            t_99 = 4.60
        if n == 40:
            t_95 = 2.02
            t_99 = 2.70
        if n== 120:
            t_95 = 1.98
            t_99 = 2.62
        # Finding upper and lower limits
        lowerLimit_t95 = mean_s-t_95*stddev_s/(n**0.5)
        upperLimit_t95 = mean_s+t_95*stddev_s/(n**0.5)

        lowerLimit_t99 = mean_s-t_99*stddev_s/(n**0.5)
        upperLimit_t99 = mean_s+t_99*stddev_s/(n**0.5)

        if mean >= lowerLimit_n95 and mean <= upperLimit_n95:
            successes_n95 = successes_n95 + 1
        if mean >= lowerLimit_t95 and mean <= upperLimit_t95:
            successes_t95 = successes_t95 + 1

        if mean >= lowerLimit_n99 and mean <= upperLimit_n99:
            successes_n99 = successes_n99 + 1
        if mean >= lowerLimit_t99 and mean <= upperLimit_t99:
            successes_t99 = successes_t99 + 1
        # Calculating the sucess for 99 and 95
        successes_n95 = successes_n95 / M * 100
        successes_t95 = successes_t95 / M * 100

        successes_n99 = successes_n99 / M * 100
        successes_t99 = successes_t99 / M * 100
        # Print results
        print("Normal Confidence 95% n =",n,":",successes_n95)
        print("Student Confidence 95% n =",n,":",successes_t95)

        print("Normal Confidence 99% n =",n,":",successes_n99)
        print("Student Confidence 99% n =",n,":",successes_t99)
ConfInterval(5)
ConfInterval(40)
ConfInterval(120)
