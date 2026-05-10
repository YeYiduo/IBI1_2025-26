
from math import ceil
a=int(input("Enter the number of infected individuals: ")) # e.g. if there are 10 infected individuals, enter 10
b=float(input("Enter the growth rate: ")) # e.g. if the growth rate is 5%, enter 0.05
c=0 
d=0
while d<=91: # the number of infected individuals is less than or equal to 91
    c+=1 # increase the day by 1
    d=a*(1+b)**c # calculate the number of infected individuals on day c
    if d>=91:
        print("Day", c+1, ":", ceil(91), "infected individuals")
        break
    print("Day", c+1, ":", ceil(d), "infected individuals")

print("The population will reach 91 infected individuals on day", c+1)
    

