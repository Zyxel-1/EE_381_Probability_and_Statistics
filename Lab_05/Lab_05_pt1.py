# -------------------------------
# Name: Roberto Sanchez
# Date: November 12, 2017
# Assignment 05 - Confidence Intervals
# Part 1 - Effect of sample size on confidence intervals
# -------------------------------
import numpy as np
import matplotlib.pyplot as plt
def SampleConfInterval(sampleSize):
    # Declaring given data
    totalBearings = 1000000
    popMean = 75
    popStdDev = 7.5
    # Calculate
    bearings = np.random.normal(popMean,popStdDev,totalBearings)
    result = []
    for i in range(sampleSize):
        sample = np.random.choice(bearings,(i+1))
        result.append(sum(sample) / (i+1))
    # Z-Values for Conf. Intervals
    z_95 = 1.95
    z_99 = 2.57
    # Plotting Figure 1
    plt.figure(1)
    plt.title("Sample Means and 95% Confidence Intervals")
    plt.xlabel("Sample Size")
    plt.ylabel("x_bar")
    plt.barh(popMean,sampleSize,height=0.5,color="black")
    # Creating evenly spaced numbers over a specific Intervals
    x = np.linspace(1,sampleSize)
    plt.plot(x,popMean+z_95*popStdDev/(x**(1/2)),color="red",linestyle='--')
    plt.plot(x,popMean-z_95*popStdDev/(x**(1/2)),color="red",linestyle='--')
    plt.scatter(range(sampleSize),result,marker='x')
    plt.show()
    # Plotting Figure 2
    plt.figure(2)
    plt.title("Sample Means and 99% Confidence Intervals")
    plt.xlabel("Sample Size")
    plt.ylabel("x_bar")
    plt.barh(popMean,sampleSize,height=0.5,color="black")
    # Creating evenly spaced numbers over a specific Intervals
    x = np.linspace(1,sampleSize)
    plt.plot(x,popMean+z_99*popStdDev/(x**(1/2)),color="green",linestyle='--')
    plt.plot(x,popMean-z_99*popStdDev/(x**(1/2)),color="green",linestyle='--')
    plt.scatter(range(sampleSize),result,marker='x')
    plt.show()
SampleConfInterval(200)
