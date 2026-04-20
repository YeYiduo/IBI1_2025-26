import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
plt.figure(figsize=(6, 4), dpi=150)
for v in range(0, 110, 10):
    S = 9999
    I = 1
    R = 0
    if v > 0:
        vaccinated = np.random.binomial(S, v / 100)
        S -= vaccinated
        R += vaccinated
    
    I_list = [I]
    for t in range(time_steps):
        new_infected = np.random.binomial(S, beta * I / N)
        new_recovered = np.random.binomial(I, gamma)
        
        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered
        
        I_list.append(I)
    
    plt.plot(I_list, label=f"{v}%", color=cm.viridis(v / 100))

plt.xlabel('Time Step')
plt.ylabel('Number of Infected Individuals')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend(title='Vaccination Rate')
plt.savefig('SIR_vaccination.png')
plt.show()



