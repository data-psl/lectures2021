import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2)

plt.figure(figsize=(4, 3))
plt.plot(t, np.maximum(t, 0), linewidth=2)
plt.savefig("relu.png")
