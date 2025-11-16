import random
print("Welcome to Blackjack!")
print("Start?")
print("Press + to start.")
while True:
    if input()=="+":
        break
    print("Press + to start.")
while True:
    try:
        PNum=int(input("Num Players?(1-8):"))
        if 1<=PNum<=8:
            break
        else:
            print("Num Players?(1-8):")
    except ValueError:
        print("Num Players?(1-8):")
balances=[]
for i in range(PNum):
    balances.append(500)
print("Start Balance: 500")
print("Goal:")
print("Reach 50,000")
def game():
    bets=[]
    results=[]
    for i in range(PNum):
        results.append(-1)
    bets = []
    for i in range(PNum):
        while True:
            try:
                print("Enter bet for Player",i+1)
                bet=int(input())
                bets.append(bet)
                break         
            except ValueError:
                print("Please enter a"\
                      "Valid integer.")
    suits=('Hearts','Diamonds','Spades','Clubs')
    cards=('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
    values={
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
    deck=[]
    d_hand=[]
    hands=[]
    for i in range(PNum):
        hands.append([])
    single_deck=[c+" of "+s for s in suits for c in cards]
    deck=single_deck*8
    random.shuffle(deck)
    def tot(hand):
        t=0
        aces=0
        for card in hand:
            name=card.split(" ")[0]
            t+=values[name]
            if name=="Ace":
                aces+=1
        while t>21 and aces>0:
            t-=10
            aces-=1
        return t
    def show(hand,n):
        print("")
        if hand is d_hand:
            print("Dealer's Hand:")
        else:
            print("Player", n+1, "Hand:")
        for c in hand:
            print(c)
    def dealer():
        while tot(d_hand)<17:
            print("Dealer hits.")
            d_hand.append(deck.pop())
            show(d_hand,-1)
            print("Total:", tot(d_hand))
            print("")
    def checkwinner(n):
        dealer_total=tot(d_hand)
        player_total=tot(hands[n])

        if dealer_total>21:
            dealer_total=0

        if player_total>dealer_total:
            print("Player",n+1,"wins!")
            return 1
        elif player_total<dealer_total:
            print("Dealer wins against Player",n+1)
            return 0
        else:
            print("Player",n+1,"ties!")
            return 2
    def check_end(n):
        total=tot(hands[n])
        if total==21:
            print("Blackjack!")
            dealer()
            return checkwinner(n)
        elif total>21:
            print("Bust!")
            return 0
        return -1
    for i in range(PNum):
        hands[i].append(deck.pop())
    d_hand.append(deck.pop())
    for i in range(PNum):
        hands[i].append(deck.pop())
    d_hand.append(deck.pop())
    for i in range(PNum):
        print("Player",i+1)
        print("Press + to See Hand")
        while True:
            if input()=="+":
                break
        show(hands[i], i)
        print("Total value:",tot(hands[i]))
        r=check_end(i)
        if r!=-1:
            results[i]=r
        print("Press + When Done")
        while True:
            if input()=="+":
                break
            print("Press + When Done")
        print("\n"*20)
    for i in range(PNum):
        if results[i]!=-1:
            continue
        print("Player", i+1)
        hs=input("Hit or Stand?(+/-):")
        while hs not in ("+","-"):
            hs=input("Hit or Stand?(+/-):")
        while hs=="+":
            hands[i].append(deck.pop())
            show(hands[i], i)
            print("Total value:",tot(hands[i]))
            r=check_end(i)
            if r!=-1:
                results[i]=r
                break
            hs=input("Hit or Stand?(+/-):")
    active=False
    for r in results:
        if r==-1:
            active=True
    if active:
        dealer()
    for i in range(PNum):
        if results[i]==-1:
            results[i]=checkwinner(i)
    return results,bets
def update_balances(results,bets):
    for i in range(PNum):
        if results[i]==1:
            balances[i]+=bets[i]
        elif results[i]==0:
            balances[i]-=bets[i]
    for i in range(PNum):
        print("Player",i+1,"Balance:",balances[i])
def balancecheck():
    winners = []
    bankrupts = []
    for i,bal in enumerate(balances):
        if bal>=50000:
            winners.append(i+1)
        elif bal<=0:
            bankrupts.append(i+1)
    if winners:
        if len(winners)==1:
            print("Player",winners[0],"has reached 50,000!")
        else:
            print("Players",", ".join(str(w) for w in winners),"have reached 50,000!")
        print("Goal Reached")
        print("GAME OVER")
        return True
    if bankrupts:
        if len(bankrupts)==1:
            print("Player", bankrupts[0], "is bankrupt.")
        else:
            print("Players",", ".join(str(b) for b in bankrupts),"are bankrupt.")
        print("GAME OVER")
        return True
    return False
results,bets=game()
update_balances(results,bets)
if balancecheck():
    pass
else:
    more=input("Play Again?(+/-)")
    while more not in ("+","-"):
        more=input("Play Again?(+/-)")
    while more=="+":
        results,bets=game()
        update_balances(results,bets)
        if balancecheck():
            break
        more=input("Play Again?(+/-)")
print("Thank You")
print("For playing!")
#By Arpith Nair
#16/11/25