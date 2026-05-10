import numpy as np
import matplotlib.pyplot as plt

# Initialize 100x100 grid: 0=Susceptible, 1=Infected, 2=Recovered
population = np.zeros((100, 100), dtype=int)

# Random initial infection
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Model parameters
beta = 0.3
gamma = 0.05
total_steps = 100

# Time points to plot (show spread and recovery process)
plot_time_points = [0, 25, 50, 75, 100]

# Main simulation loop
for t in range(total_steps + 1):
    # Plot heatmap at specified time points
    if t in plot_time_points:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap="viridis", interpolation="nearest")
        plt.colorbar(label="0: Susceptible | 1: Infected | 2: Recovered")
        plt.title(f"Spatial SIR Model - Time step {t}")
        plt.savefig(f'spatial_SIR_t{t}.png')
        plt.show()

    # Prepare new infections (synchronous update)
    new_infected = np.zeros_like(population)
    infected_rows, infected_cols = np.where(population == 1)

    # Infect 8 neighbors
    for i, j in zip(infected_rows, infected_cols):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue  # Skip self
                ni, nj = i + di, j + dj
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if population[ni, nj] == 0 and np.random.rand() < beta:
                        new_infected[ni, nj] = 1

    # Recovery process
    new_recovered = (population == 1) & (np.random.rand(100, 100) < gamma)

    # Update population states
    population[new_infected == 1] = 1
    population[new_recovered] = 2