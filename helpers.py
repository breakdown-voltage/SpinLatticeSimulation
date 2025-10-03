import numpy as np

def calc_energy(k: float, l: np.array, N: int):
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += l[i][j] * (l[(i + 1) % N][j] + l[i][(j + 1) % N])
    return -k * sum


def Magnetisation(l, N):
  sum = 0
  for i in range(N):
    for j in range(N):
      sum+=l[i][j]
  return sum/N**2

def createLattice(N):
  spins = [-1, 1]
  lattice = np.ones((N, N))
  for i in range(N):
    for j in range(N):
      lattice[i][j] = np.random.choice(spins)
  return lattice

def f(x, k):
    return np.exp(-x/k)