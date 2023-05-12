import random
pres_top_down=0
pres_multi=1
prestige=0
top=250-pres_top_down
value=random.randint(1,top)
guesses=1
play_again="Yes"
balance=0
multi=pres_multi
top_cost=1
multi_cost=10
total_cost=0
limit=top
flag="no"
while top>1:
    guess=input("Guess a number 1 through "+str(top)+" ")
    while not guess.isdecimal() or guess=="":
                guess=input("Try again ")
    repeat="Yes"
    while repeat=="Yes":
        if int(guess)>value:
            guess=input("Try a lower guess ")
            while not guess.isdecimal() or guess=="":
                guess=input("Try again ")
            guesses+=1
        elif int(guess)<value:
            guess=input("Try a higher guess ")
            while not guess.isdecimal() or guess=="":
                guess=input("Try again ")
            guesses+=1
        else:
            print("Congratulations! You guessed the number in",guesses,"guesses!")
            balance+=100//guesses*multi
            print("+"+str(100//guesses*multi),"coins! Your balance is now",balance,"coins!")
            guesses=1
            repeat="No"
    upgrades=input("Want to buy some upgrades? ")
    while not upgrades=="Yes" and not upgrades=="yes" and not upgrades=="No" and not upgrades=="no":
        if upgrades=="cheat code!" and flag=="no":
                balance+=1000
                flag="yes"
                print("You found a cheat code! Your balance is now",balance)
        upgrades=input("Make up your mind already! ")
    while upgrades=="Yes" or upgrades=="yes":
        print("You have",balance,"coins.")
        print("Decrease maximum value by 1:",str(top_cost)+" coins (increases by 1 every purchase)")
        print("Multiplies payout by 2:",str(multi_cost)+" coins (triples in price every purchase)")
        buy=input("What'll it be? (Type max or multi or neither) ")
        while not buy=="max" and not buy=="multi" and not buy=="neither":
            buy=input("Type max or multi or neither ")
        if buy=="max":
            how_many=input("How many do you want? ")
            while not how_many.isdecimal():
                how_many=input("Type an integer ")
            if int(how_many)>limit:
                print("That's a lot! Try something less.")
            elif how_many=="0":
                print("So you changed your mind")
            else:
                for i in range(int(how_many)):
                    total_cost+=top_cost
                    top_cost+=1
                if total_cost<=balance:
                    confirm=input("That will be "+str(total_cost)+". Confirm? (Type yes or no) ")
                    while not confirm=="yes" and not confirm=="no":
                        confirm=input("Type yes or no ")
                    if confirm=="yes":
                        top-=int(how_many)
                        print("Congrats, your top is now",top)
                        balance-=total_cost
                        total_cost=0
                    else:
                        print("Aight consider it cancelled")
                        total_cost=0
                        top_cost-=int(how_many)
                else:
                    print("That costs",total_cost,"coins and you have",balance,"coins. Go make some money!")
                    total_cost=0
                    top_cost-=int(how_many)
        elif buy=="multi":
            how_many=input("How many do you want? ")
            while not how_many.isdecimal():
                how_many=input("Type an integer ")
            if int(how_many)>5:
                print("That's a lot! Try something less. ")
            elif how_many=="0":
                print("So you changed your mind")
            else:
                for i in range(int(how_many)):
                    total_cost+=multi_cost
                    multi_cost*=3
                if total_cost<=balance:
                    confirm=input("That will be "+str(total_cost)+". Confirm? (Type yes or no) ")
                    while not confirm=="yes" and not confirm=="no":
                        confirm=input("Type yes or no ")
                    if confirm=="yes":
                        multi*=2**int(how_many)
                        print("Congrats, your multiplier is now",multi)
                        balance-=total_cost
                        total_cost=0
                    else:
                        print("Aight consider it cancelled")
                        total_cost=0
                        multi_cost=multi_cost//(3**(int(how_many)))
                else:
                    print("That costs",total_cost,"coins and you have",balance,"coins. Go make some money!")
                    total_cost=0
                    multi_cost=multi_cost//(3**(int(how_many)))
        else:
            print("Ok see you next time!")
            upgrades="no"
    if top<=1:
        print("WOW!!! You beat the game! Congratulations! You are now prestiging!")
        pres_upgrade=input("Do you want to permanantly decrease max guess by 50 or multiply your payout permanantly by 2? (type max or multi) ")
        while not pres_upgrade=="max" and not pres_upgrade=="multi":
            pres_upgrade=input("type max or multi")
        if pres_upgrade=="max":
            pres_top_down+=50
        else:
            pres_multi*=2
        prestige+=1
        print("You are now prestige",prestige)
        top=250-pres_top_down
        multi=pres_multi
        top_cost=1
        multi_cost=10
        total_cost=0
        balance=0
        if top<=1:
            print("Wow!!! You super beat the game! Awesome!")
            break
    value=random.randint(1,top)
