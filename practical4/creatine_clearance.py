
import sys
a=input("Enter your gender: ") # e.g. if you are female, enter "female", if you are male, enter "male"
b=input("Enter your age: ") 
c=input("Enter your weight in kg: ")  
d=input("Enter your  creatinine concentration in µmol/l: ") 
if int(b)<100 and 20<int(c)<80 and 0<float(d)<100 and (a=="female" or a=="male"):
    print("Your input is valid.")
else:
    print("Your input is invalid. Please enter valid inputs.")
    sys.exit()
if a=="female":
    creatinine_clearance=(140-int(b))*int(c)*0.85/(72*float(d))
    print("Your creatinine clearance is: ",creatinine_clearance)
else:
    creatinine_clearance=(140-int(b))*int(c)/(72*float(d))
    print("Your creatinine clearance is: ",creatinine_clearance)
