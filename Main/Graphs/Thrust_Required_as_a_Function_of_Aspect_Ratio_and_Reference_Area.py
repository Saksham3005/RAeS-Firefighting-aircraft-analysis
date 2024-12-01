import numpy as np
import matplotlib.pyplot as plt

# Define constants
rho = 1.293  # air density at sea level in kg/m^3
V = 83  # flight speed in m/s
CL = 0.82  # assumed constant lift coefficient
CD0 = 0.006  # zero-lift drag coefficient
e = 0.8  # Oswald efficiency factor

# Define ranges for AR and Sref
AR = np.linspace(5, 15, 100)
Sref = np.linspace(30, 50, 100)

# Create meshgrid for plotting
AR_grid, Sref_grid = np.meshgrid(AR, Sref)

# Calculate CD
CD = CD0 + (CL**2) / (np.pi * AR_grid * e)

# Calculate drag
D = 0.5 * rho * V**2 * Sref_grid * CD
W = 86180
E = 26.4

# Calculate thrust required
T = D*1e3 / (CL/CD)
print(D)
print(T)
# Plot the results as a 2D color gradient

plt.figure(figsize=(10, 7))
plt.contourf(Sref_grid, AR_grid, T, levels=100, cmap='viridis')
plt.colorbar(label='Thrust Required (T)')

# Add labels and title
plt.xlabel('Reference Area (Sref)')
plt.ylabel('Aspect Ratio (AR)')

plt.title('Thrust Required')
# Show the plot
plt.show()