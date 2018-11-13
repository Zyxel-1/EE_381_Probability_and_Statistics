#----------------------------------------------------------
# Name: Roberto Sanchez
# Date: December 07, 2017
# Assignment 6 - Markov Chains
#----------------------------------------------------------
def PageRank(N,n):
    X = np.chararray((n,N))
    X[:] = 0
    P = np.matrix([[0,1,0,0,0],[1/2,0,1/2,0,0],[1/3,1/3,0,0,1/3],[1,0,0,0,0],[0,1/3,1/3,1/3,0]])
    V = np.matrix([[1/5,1/5,1/5,1/5,1/5],[0,0,0,0,1]])
    for i in range(0,2):
        s0 = V[i,:]
        Y = np.zeros((n,5))
        Y[0,:] = s0;
        for j in range(0,n-1):
            Y[j+1,:] = np.matmul(Y[j,:],P)
        nv = np.linspace(0,n,num=20)
        plt.figure()
        plt.plot(nv,Y,marker='o',markersize=6)
        plt.title(('PageRank Probabilities: s0= ',np.str(s0)))
        plt.xlabel('Time step (n)')
        plt.ylabel('Probability of page visit')
        plt.legend((['A'],['B'],['C'],['D'],['E']))
        plt.show
PageRank(10000,20)
