import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 10)

# Original function
f_n = 12 * n**3 + 7 * n**2 + 4 * n + 4

big_O = 27 * n**3
big_omega = 12 * n**3
small_w = 12 * n**2.5
small_o = 12 * n**3.5

plt.figure(figsize=(8, 5))
plt.plot(n, f_n, label=r'$f(n) = 12n^3 + 7n^2 + 4n + 4$', color='blue', linewidth=2)
plt.plot(n, big_O, label=r'$O(n^3) = 27n^3$', color='red', linestyle='--', linewidth=2)
plt.plot(n, big_omega, label=r'$\Omega(n^3) = 12n^3$', color='green', linestyle=':', linewidth=2)
plt.plot(n, small_w, label=r'$\omega(n^{2.5}) = 12n^{2.5}$', color='pink', linestyle=':', linewidth=2)
plt.plot(n, small_o, label=r'$o(n^{3.5}) = 12n^{3.5}$', color='orange', linestyle=':', linewidth=2)


plt.xlabel('n')
plt.ylabel('Function Value')
plt.title('f(n) with Big-O and Big-Ω Bounds')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.show()
