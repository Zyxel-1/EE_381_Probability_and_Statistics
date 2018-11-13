#----------------------------------------------
#   Name: Roberto Sanchez
#   Date: December 07, 2017
#   Assignement 6 - Markov Chains
#------------Importing packages-----------------
import numpy as np
import matplotlib.pyplot as plt
import random
# MarkovChain Definition
def MarkovChain(N,n):
    S = [0 for i in range(0,n)]
    X = np.chararray((n,N))
    X[:] = 0
    M = np.zeros((n,3))
    prob = {'p11' : 1/3, 'p12' : 1/3, 'p13' : 1/3, 'p21' : 1/2, 'p23' : 1/2, 'p22' : 0, 'p31' : 1/4, 'p32' : 1/4, 'p33' : 1/2}
    dist = {'d01' : 1/4, 'd03' : 1/4, 'd02' : 1/2}
    for j in range(0,N):
        r0 = np.random.random();
        if r0 <= dist['d01']:
            s0 = 'R'
        elif r0>dist['d01'] and r0<=dist['d01']+dist['d02']:
            s0 = 'N'
        elif r0>dist['d01']+dist['d02']:
            s0 = 'S'
        S[0] = s0
#
        for k in range(0,n-1):
            s = S[k]
            r = np.random.random();
            if s == 'R':
                if r<=prob['p11']:
                    S[k+1]='R'
                elif r>prob['p11'] and r<=prob['p11']+prob['p12']:
                    S[k+1]='N'
                elif r>prob['p11']+prob['p12']:
                    S[k+1]='S'
            elif s == 'N':
                if r<=prob['p21']:
                    S[k+1]='R'
                elif r>prob['p21'] and r<=prob['p21']+prob['p22']:
                    S[k+1]='N'
                elif r>prob['p21']+prob['p22']:
                    S[k+1]='S'
            elif s == 'S':
                if r<=prob['p31']:
                    S[k+1]='R'
                elif r>=prob['p31'] and r<=prob['p31']+prob['p32']:
                    S[k+1]='N'
                elif r>prob['p31']+prob['p32']:
                    S[k+1]='S'
        X[:,j]=S
    for j in range(0,n):
        ma=0
        mb=0
        mc=0
        x=X[j,:]
        for i in range(N):
            if str(x[i],'utf-8') == 'R':
                ma += 1
        for p in range(N):
            if str(x[p],'utf-8') == 'N':
                mb += 1
        for q in range(N):
            if str(x[q],'utf-8') == 'S':
                mc += 1
        M[j,:] = [ma/N,mb/N,mc/N]

# ---------------------------------Plot-------------------------------------
    plt.figure(1)
    nv = np.linspace(0,n,num=15)
    plt.plot(nv,M[:,0],color = 'blue',marker='*',markersize=6)
    plt.plot(nv,M[:,1],color = 'green',marker='+',markersize=6)
    plt.plot(nv,M[:,2],color = 'red',marker='^',markersize=6)
    plt.title('Simulation results -- States R,N,S')
    plt.xlabel('Time step (n)')
    plt.ylabel('Prob (State)')
    plt.legend((['State R'],['State N'],['State S']))
    plt.show()
    P = np.matrix([[prob['p11'],prob['p12'],prob['p13']],[prob['p21'],prob['p22'],prob['p23']],[prob['p31'],prob['p32'],prob['p33']]])
    y0 = np.matrix([1/4,1/2,1/4])
    Y = np.zeros((n,3))
    Y[0,:] = y0
    for k in range(0,n-1):
        Y[k+1,:] = np.matmul(Y[k,:],P)
    # Figure 2 Chart
    plt.figure(2)
    plt.plot(nv,Y[:,0],color = 'blue',marker='o',markersize=6)
    plt.plot(nv,Y[:,1],color = 'green',marker='o',markersize=6)
    plt.plot(nv,Y[:,2],color = 'red',marker='o',markersize=6)
    plt.title('Results based on State Transition Matix -- States R,N,S')
    plt.xlabel('Time step(n)')
    plt.ylabel('Prob(State)')
    plt.legend((['State R'],['State N'],['State S']))
    plt.show()
MarkovChain(10000,15)
