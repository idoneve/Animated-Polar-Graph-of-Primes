import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

primes, x = [i for i in range(0, 100000) if is_prime(i)], []
def animate(i):
    x.append(primes[i])
    ax.clear()
    plt.polar(x, 'o', markersize=2)

anim = animation.FuncAnimation(fig, animate, frames=len(primes), interval=1, repeat=False)

plt.grid()
plt.show()
