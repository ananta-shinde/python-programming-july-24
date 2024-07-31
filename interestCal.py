
p = int(input("enter priciple ammount : "))
n = int(input("enter n of years of investment : "))
r = float(input("enter expected rate of interest : "))

si = (p*n*r)/100
amount = p + si

# print("your invested money is "+str(p)+",interest earned :"+str(si)+", final amount"+str(amount))
# message =
print("your invested money is {x},interest earned :{y}, final amount:{z}".format(x=p,y=si,z=amount))

