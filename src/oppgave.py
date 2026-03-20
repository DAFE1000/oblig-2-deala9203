import numpy as np
import matplotlib.pyplot as plt

# Funksjonen f(x)
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# Ligningen som skal være lik 0
def g(x):
    return np.arctan(x) - 4/(1 + x**2)

# Binærsøk for å finne rot
a, b = 0, 5
for _ in range(100):
    mid = (a + b) / 2
    if g(a) * g(mid) <= 0:
        b = mid
    else:
        a = mid

x_max = (a + b) / 2
y_max = f(x_max)

print(f"x_max = {x_max:.4f}")
print(f"f(x_max) = {y_max:.4f}")


