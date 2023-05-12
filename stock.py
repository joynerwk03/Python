stock = "                                                                                     "
nothing=""
import random
while len(stock)>1:
    length=len(stock)
    stock=nothing
    for i in range(0,random.randint(-8,7)//2+length):
        stock+=" "
    print(stock+"I")
    diff=length-len(stock)
    for i in range(0,random.randint(2,6)):
        if diff<len(stock):
            length_2=len(stock)
            stock=nothing
            for i in range(0,length_2-diff):
                stock+=" "
            print(stock+"I")
        else:
            break
            
