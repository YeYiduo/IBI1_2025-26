a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
print("d>=e=", d>=e)
if d>=e:
    print("the population is decelerating")
else:
    print("the population is accelerating")

X=True
Y=False
W=X or Y 
print("W=", W)