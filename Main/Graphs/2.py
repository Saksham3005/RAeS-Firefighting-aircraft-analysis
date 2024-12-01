import numpy as np
import matplotlib.pyplot as plt

# Define constants
W = 10000  # Aircraft weight in Newtons (example value)
rho = 1.225  # Air density at sea level in kg/m^3

# Maximum lift coefficient (assumed to be a function of AR for simplicity)
def CL_max(AR):
    return 1.2 + 0.1 * (AR - 6)  # Example function; adjust based on real data

# Define ranges for AR and Sref
AR = np.linspace(5, 15, 100)  # Aspect ratio from 5 to 15
Sref = np.linspace(35, 45, 100)  # Reference area from 10 to 50 m^2

# Create meshgrid for plotting
AR_grid, Sref_grid = np.meshgrid(AR, Sref)

# Calculate CL_max for each AR value
CL_max_grid = CL_max(AR_grid)

# Calculate stall speed
V_stall = np.sqrt((2 * W) / (rho * Sref_grid * CL_max_grid))

# Plot the results as a 2D color gradient
plt.figure(figsize=(10, 7))
plt.contourf(AR_grid, Sref_grid, V_stall, levels=50, cmap='coolwarm')
plt.colorbar(label='Stall Speed (m/s)')

# Add labels and title
plt.xlabel('Aspect Ratio (AR)')
plt.ylabel('Reference Area (Sref)')
plt.title('Stall Speed as a Function of Aspect Ratio and Reference Area')

# Show the plot
plt.show()
