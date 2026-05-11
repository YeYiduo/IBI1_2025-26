import numpy as np
import matplotlib.pyplot as plt
N=10000
beta=0.3
gamma=0.05
S=9999
I=1
R=0
S_list=[S]
I_list=[I]
R_list=[R]
for t in range(1000):
    new_infected=np.random.binomial(S, beta*I/N)
    new_recovered=np.random.binomial(I, gamma)
    S-=new_infected
    I+=new_infected-new_recovered
    R+=new_recovered
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S_list, label='susceptible')
plt.plot(I_list, label='infected')
plt.plot(R_list, label='recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title("SIR model")
plt.legend()
plt.savefig('SIR.png')
plt.show()
