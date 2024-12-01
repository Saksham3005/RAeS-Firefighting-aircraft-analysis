import numpy as np
import matplotlib.pyplot as plt

# Define constants
V = 250  # Velocity in m/s (example value)
c = 0.0002  # Specific fuel consumption in 1/s (example value)
g = 9.81  # Acceleration due to gravity in m/s^2
Wi = 50000  # Initial weight in Newtons (example value)
Wf = 30000  # Final weight in Newtons (example value)
rho = 1.225  # Air density at sea level in kg/m^3
CD0 = 0.02  # Zero-lift drag coefficient
e = 0.8  # Oswald efficiency factor

# Define ranges for AR and Sref
AR = np.linspace(5, 15, 100)  # Aspect ratio from 5 to 15
Sref = np.linspace(35, 45, 100)  # Reference area from 10 to 50 m^2

# Create meshgrid for plotting
AR_grid, Sref_grid = np.meshgrid(AR, Sref)

# Calculate CL for level flight
CL = (2 * Wi) / (rho * V**2 * Sref_grid)

# Calculate CD using the aspect ratio
CD = CD0 + (CL**2) / (np.pi * AR_grid * e)

# Calculate lift-to-drag ratio (L/D)
L_D = CL / CD

# Calculate ferry range using the Breguet range equation
R = (V / c) * (L_D / g) * np.log(Wi / Wf)

# Plot the results as a 2D color gradient
plt.figure(figsize=(10, 7))
plt.contourf(AR_grid, Sref_grid, R, levels=50, cmap='plasma')
plt.colorbar(label='Ferry Range (m)')

# Add labels and title
plt.xlabel('Aspect Ratio (AR)')
plt.ylabel('Reference Area (Sref)')
plt.title('Ferry Range as a Function of Aspect Ratio and Reference Area')

# Show the plot
plt.show()
