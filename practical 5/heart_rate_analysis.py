heart_rates=[72,60,	126,85,	90,	59,	76,	131,88,	121,64]
mean_heart_rate=sum(heart_rates)/len(heart_rates)
print("the total patients is:", len(heart_rates))
print(f"The mean heart rate is: {mean_heart_rate:.2f} bpm")
low=[]
normal=[]
high=[]
for i in heart_rates:
    if i<60:
        low.append(i)
    elif 60<=i<=120:
        normal.append(i)
    else:        
        high.append(i)
a=max(len(low), len(normal), len(high))
print("The largest category is:", end=" ")
if len(low)==a:
    print("Low heart rate") 
elif len(normal)==a:
    print("Normal heart rate")      
else:    
    print("High heart rate")
import matplotlib.pyplot as plt
import numpy as np
categories = ['Low', 'Normal', 'High']
counts = [len(low), len(normal), len(high)]
sizes = [count / sum(counts) * 100 for count in counts]
plt.pie(sizes, labels=categories,autopct="%1.1f%%", colors=['blue', 'green', 'red'])
plt.title("Distribution of Heart Rates categories")
plt.show()

