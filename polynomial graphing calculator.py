coefficients=[]
powers=[]
more="Yes"
print("Enter a term:")
terms=0
while more=="Yes" or more=="yes":
    terms+=1
    coefficients.append(input("What coefficient? "))
    powers.append(input("What power? "))
    more=input("Add another term? ")
start=float(input("Where do you want to start? "))
end=float(input("Where do you want to end? "))
y=0
len_domain=end-start
ys=[]
xs=[]
for x in range(0,61):
    for integer in range(0,terms):
        y+=float(coefficients[integer])*((x/60*len_domain+start)**float(powers[integer]))
    ys.append(y)
    xs.append(x/60*len_domain+start)
    y=0
max=float(coefficients[integer])*((start)**float(powers[integer]))
min=float(coefficients[integer])*((start)**float(powers[integer]))
for height in ys:
    if float(height)>max:
        max=float(height)
    elif float(height)<min:
        min=float(height)
y_range=max-min
print("Turn your head!")
y_str="          "+str(round(min,4))
for i in range(1,17):
    while len(y_str)<(10*i+10):
        y_str+=" "
    y_str+=str(round(y_range*i/16+min,10-len(str(round(y_range*i/16+min,4)))))
print(y_str)
print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
for i in range(0,61):
    x_str=""
    if (i%4)==0:
        x_str+=str(round(float(xs[i]),4))
    while len(x_str)<9:
        x_str+=" "
    x_str+="I"
    while len(x_str)<(10+round((ys[i]-min)/y_range*160)):
        x_str+=" "
    x_str+="|"
    print(x_str)

    
