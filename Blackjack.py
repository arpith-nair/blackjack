import random
print("Welcome to Blackjack!")
print("Start?")
print("Press + to start.")
while True:
    if input() == "+":
        break
    print("Press + to start.")
print("Start Balance: 500")
Balance=500
print("Goal:")
print("Reach 50,000")
def game(): 
    global win,Bet
    while True:
        try:
            Bet=int(input("Bet Value?"))
            break
        except ValueError:
            print("Please enter a")
            print("Valid Integer.")
    win=-1
    suits = ('Hearts','Diamonds','Spades','Clubs')
    cards = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
    values = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
    }
    deck = []
    p_hand=[]
    d_hand=[]
    for i in suits:
        for j in cards:
            card=(j + " of " + i)
            deck.append(card)
    random.shuffle(deck)
    def tot(k):
        tot=0
        aces=0
        totl=len(k)
        for v in range(totl):
            c_v=k[v].split(" ")[0]
            tot+=values[c_v]
            if c_v=="Ace":
                aces+=1
        while tot>21 and aces>0:
            tot-=10
            aces-=1        
        return tot
    def show(k):
        print("\n")
        if k is d_hand:
            print("Dealer\'s Hand:")
            for m in k:
                print(m)
        else:
            print("Your Hand:")
            for m in k:
                print(m)        
    def dealer():
        while tot(d_hand)<17:
            print("Dealer hits.")
            d_hand.append(deck.pop())
            show(d_hand)
            print("Total:",tot(d_hand))
            print("\n")
    def checkwinner():
        global win
        show(d_hand)
        print("Total value:",tot(d_hand))
        if tot(d_hand)>21:
            print("Dealer Bust!")
            dval=0
        else:
            dval=tot(d_hand)    
        if tot(p_hand)>dval:
            print("You Win!")
            win=1
        elif tot(p_hand)<dval:
            print("Dealer Won")
            win=0
        else:
            print("Tie!")
            win=2
        return
    def check_end():
        total = tot(p_hand)
        if total == 21:
            print("Blackjack!")
            dealer()
            checkwinner()
            return True
        elif total > 21:
            print("Bust!")
            global win
            win=0
            return True
        return False
    p_hand.append(deck.pop())
    d_hand.append(deck.pop())
    p_hand.append(deck.pop())
    d_hand.append(deck.pop())
    show(p_hand)
    print("Total value:",tot(p_hand))
    if check_end():
        return
    hs=input("Hit or Stand?(+/-):")
    while hs not in ("+","-"):
        hs=input("Hit or Stand?(+/-):")
    while hs=="+":
        p_hand.append(deck.pop())
        show(p_hand)
        print("Total value:",tot(p_hand))
        if check_end():
            return
        hs=input("Hit or Stand?(+/-):")
    checkwinner()
def fullcheck():
    global Balance
    if win==0:
        Balance-=Bet
    elif win==1:
        Balance+=Bet
    print("Balance:",Balance)
def balancecheck():
    if Balance>=50000:
        print("Goal Reached")
        print("Well Played")
    elif Balance<=0:
        print("Bankrupt")
        print("GAME OVER")
game()
fullcheck()
balancecheck()
more=input("Play Again?(+/-)")
while more not in ("+","-"):
    more=input("Play Again?(+/-)")
while more=='+':
    game()
    fullcheck()
    balancecheck()
    more=input("Play Again?(+/-)")
print("Thank You")
print("For playing!")
#By Arpith Nair

#15/11/2025
