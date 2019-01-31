import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

#-------------------------------------------------------------------------------
# Helper functions

# Derive the function f and evaluate it in t
def differentiate(f, t, dt=0.01):
    f_prime = (f(t + dt) - f(t))/dt
    return f_prime

# Integrate the function f and evaluate it in t
def integrate(f_prime, t0, t, f0, dt=0.01):
    f = f0
    _ = np.linspace(t0, t, int((t - t0)/dt) )
    for i in _:
        f += f_prime(i) * dt
    return f

# Vectorize differentiate
differentiate = np.vectorize(differentiate)
# Vectorize Integrate
integrate = np.vectorize(integrate)

################################################################################
#                          Quick working example
################################################################################

# Interval
#t = np.linspace(0.01, 10, 1000)

# Function
#def f(t):
#    return t**2

# Evaluate the derivative of f on the interval t   
#plt.plot(t, differentiate(f = f, t = t))
# Evaluate the integral of f on the interval t
#plt.plot(t, integrate(f_prime = f, t0 = 0, t = t, f0 = 0))
#plt.show()

#-------------------------------------------------------------------------------

M = 80      # kg Mass of the diver
RHO = 1.23  # kg/m^3 Air density
A = 0.53    # m^2 Area facing the stream of air
C = 1.05    # Adimensional drag coefficient
g = 9.81    # m/s^2
T_MAX = 20  # s Maximum time window
t = np.linspace(0.01, T_MAX, 1000)

# Position function from Wolfram Alpha
def position(t):
    y = (M / (0.5*RHO*A*C) ) * np.log( np.cosh( (np.sqrt(0.5*RHO*A*C)*np.sqrt(g) * t)/np.sqrt(M) ) )
    return y

# Calculate speed
speed = differentiate(f = position, t = t)

# Calculate acceleration
acceleration = g - (0.5*RHO*A*C / M)*speed**2

# Plot
plt.plot(t, position(t), label = 'Position m')
plt.plot(t, speed, label = 'Speed m/s')
plt.plot(t, acceleration, label = 'Acceleration m/s^2', color = 'green')
plt.xlim([t[0], t[-1]])
plt.xlabel("Time (seconds)")
plt.legend()

plt.show()

print("Vmax after %s seconds: %0.02f m/s (%0.02f km/h)" %(t[-1], speed[-1], speed[-1]*3.6))

################################################################################
#                               OUTPUT
################################################################################
#
# Vmax after 20.0 seconds: 47.86 m/s (172.29 km/h)
#