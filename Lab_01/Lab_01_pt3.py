# --------------------------------------
# Name: Roberto Sanchez (014587792)
# Date: Sept 16, 2017
# Assignment 1 - Part 3
# --------------------------------------
from random import randint
from random import shuffle
class card:
    def __init__(self,rank,suite):
        self.rank = rank
        self.suite = suite
    def getRank(self):
        return self.rank
    def getSuite(self):
        return self.suite
    def __str__(self):
        return ('{0} of {1}'.format(self.rank,self.suite))
    def __repr__(self):
        return ('{0} of {1}'.format(self.rank,self.suite))

def drawingCards():
    # Could be easier just to make a 2d array...too late
    cardRank = ['Ace',1,2,3,4,5,6,7,8,9,'Jack','Queen','King']
    cardSuit = ["Clubs","Spades","Hearts","Diamonds"]
    shuffle(cardRank)
    shuffle(cardSuit)

    deck = []
    for x in range(0,5):
        myCard = card(cardRank[randint(0,12)],cardSuit[randint(0,3)])
        #print(myCard)
        deck.append(myCard)
    #print("Deck",deck)

    # Calculating 4 of a kind
    #Tracks each suite
    numClubs = 0
    numSpades = 0
    numHearts = 0
    numDiamonds = 0

    # Iterates through deck tabulating suite occurances
    for x in range(0,5):
        if deck[x].getSuite() == "Clubs":
            numClubs= numClubs + 1
        elif deck[x].getSuite() == "Spades":
            numSpades= numSpades + 1
        elif deck[x].getSuite() == "Hearts":
            numHearts= numHearts + 1
        elif deck[x].getSuite() == "Diamonds":
            numDiamonds= numDiamonds + 1
    #Calculating Rank
    nA = 0
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    n7 = 0
    n8 = 0
    n9 = 0
    nj = 0
    nq = 0
    nk = 0
    for x in range (0,5):
        if deck[x].getRank() == 'Ace':
            nA = nA + 1
        elif deck[x].getRank() == 1:
            n1 = n1 + 1
        elif deck[x].getRank() == 2:
            n2 = n2 + 1
        elif deck[x].getRank() == 3:
            n3 = n3 + 1
        elif deck[x].getRank() == 4:
            n4 = n4 + 1
        elif deck[x].getRank() == 5:
            n5 = n5 + 1
        elif deck[x].getRank() == 6:
            n6 = n6 + 1
        elif deck[x].getRank() == 7:
            n7 = n7 + 1
        elif deck[x].getRank() == 8:
            n8 = n8 + 1
        elif deck[x].getRank() == 9:
            n9 = n9 + 1
        elif deck[x].getRank() == "Jack":
            nj = nj + 1
        elif deck[x].getRank() == "Queen":
            nq = nq + 1
        elif deck[x].getRank() == "King":
            nk = nk + 1
    #Printing Result
    #print("Results of this draw",numClubs," ",numSpades," ",numHearts," ",numDiamonds)
    #Checking for 4 of a kind, if true return 1 for success
    """
    if numClubs == 4 or numSpades == 4 or numHearts == 4 or numDiamonds == 4:
        return 1
    """
    if nA == 4 or n1 == 4 or n2 == 4 or n3 == 4 or n4 == 4  or n5 == 4 or n6 == 4 or n7 == 4 or n8 == 4 or n9 == 4:
        return 1
    elif nj == 4 or nq == 4 or nk == 4:
        return 1
    else:
        return 0
def experiment(N):
    result = []
    for x in range(0,N):
        res = drawingCards()
        result.append(res)
   # print("list", result)
    prob = sum(result)/N
    print("Probability of getting 4 of a kind in  100,000 trails are ",prob)
experiment(100000)
'''
OUTPUT:
runfile('/home/beryl/test.py', wdir='/home/beryl')
Probability of getting 4 of a kind in  100,000 trails are  0.00235

runfile('/home/beryl/test.py', wdir='/home/beryl')
Probability of getting 4 of a kind in  100,000 trails are  0.00247

runfile('/home/beryl/test.py', wdir='/home/beryl')
Probability of getting 4 of a kind in  100,000 trails are  0.00238

runfile('/home/beryl/test.py', wdir='/home/beryl')
Probability of getting 4 of a kind in  100,000 trails are  0.00216

'''
