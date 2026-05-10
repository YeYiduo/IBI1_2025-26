Total_Population={"UK":[66.7,69.2],"China":[1426,1410],"Italy":[59.4,58.9],"Brazil":[208.6,212.0],"USA":[331.6,340.1]}
population_growth_rates = {}
for country, population in Total_Population.items():
    growth_rate = ((population[1] - population[0]) / population[0]) * 100
    population_growth_rates[country] = growth_rate

sorted_growth_rates = sorted(population_growth_rates.items(), key=lambda x: x[1], reverse=True)
for country, growth_rate in sorted_growth_rates:
    print(f"{country}: {growth_rate:.2f}%")
print("the country with the largest increase in population is:", sorted_growth_rates[0][0])
print("the country with the largest decrease in population is:", sorted_growth_rates[-1][0])
import matplotlib.pyplot as plt
import numpy as np
countries = list(population_growth_rates.keys())
growth_rates = list(population_growth_rates.values())
plt.bar(countries, growth_rates, color=['blue', 'green', 'red', 'orange', 'purple'])
plt.xlabel('Countries')
plt.ylabel('Population Growth Rate (%)')
plt.title('Population Growth Rates from 2020 to 2024')
for i in range(len(countries)):
    plt.text(i, growth_rates[i], f"{growth_rates[i]:.2f}%", ha='center', va='bottom' if growth_rates[i] >= 0 else 'top')
plt.show()
