import math

principle = float(input("enter principle amount:"))
rate = float(input("enter rate of interest :"))
years = float(input("enter no of years of investment:"))
choice = input("enter 1 for simple interest or 2 for coumpond interest")

def calculate_simple_interest():
    simple_interest = (principle*rate*years)/100
    return simple_interest

def calculate_compound_interest():
    compound_interest = math.pow((principle+(rate/100)),years)
    return  compound_interest


if(choice == "1"):
    interest = calculate_simple_interest()
else:
    interest = calculate_compound_interest()

result = principle + interest
print("Final amount {x}".format(x=result))

