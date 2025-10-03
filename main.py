import numpy as np
import matplotlib.pyplot as plt
import argparse
from tqdm import tqdm
from helpers import createLattice, calc_energy, Magnetisation, f


class Simulator:
    def __init__(self, iters, a, b, N):
        self.iters = iters
        # Convert a and b from [min, max, num] to actual ranges
        self.a = np.linspace(a[0], a[1], int(a[2]))  # J values
        self.b = np.linspace(b[0], b[1], int(b[2]))  # KT values
        self.N = N

        # storage
        self.M_all = []
        self.E_all = []
        self.final = []
        self.start = None

    def MC(self):
        self.E_all = []
        self.M_all = []
        self.final = []

        lattice_start = createLattice(self.N)
        self.start = np.copy(lattice_start)

        for j in tqdm(self.a):
            for i in self.b:
                J = j
                K = i

                # initial energy
                E0 = calc_energy(J, lattice_start, self.N)

                E = []
                avgM = []
                lattice = np.copy(lattice_start)
                mag_sum = 0

                for _ in (range(self.iters)):
                    E.append(E0)
                    mag_sum += Magnetisation(lattice, self.N)
                    avgM.append(mag_sum / (self.N)**2)

                    # Flip a single spin
                    a1, b1 = int(self.N * np.random.rand()), int(self.N * np.random.rand())
                    lattice[a1][b1] *= -1

                    # Calculate new energy
                    E1 = calc_energy(J, lattice, self.N)

                    # Acceptance probability
                    delta_E = E1 - E0
                    acceptance = 1 if delta_E <= 0 else f(delta_E, K)

                    if np.random.rand() < acceptance:
                        E0 = E1
                    else:
                        lattice[a1][b1] *= -1  # revert

                self.final.append(lattice)
                self.M_all.append(avgM)
                self.E_all.append(E)

    def plot(self):
        plt.figure(figsize=(20, 20))
        # assume len(self.a)*len(self.b) grid
        end_mags = np.array([np.abs(k[-1]) for k in self.M_all]).reshape(len(self.a), len(self.b))

        plt.figure(figsize=(15, 7))
        for i in range(len(self.a)):
            plt.subplot(3, 3, i+1)
            plt.title(f"J = {self.a[i]:.2f}")
            plt.scatter(self.b, end_mags[i, :]/self.N**2, s=0.9)
            plt.xlabel("KT")
            plt.ylabel("Average Magnetization")
        
        plt.show()

        plt.figure(figsize=(15, 7))
        plt.title(f"Example Spin Configurations")
        plt.subplot(1, 3, 1)
        plt.imshow(self.start, cmap="gray")
        plt.title("Initial Configuration")
        plt.axis(False)

        plt.subplot(1, 3, 2)
        plt.imshow(self.final[len(self.b)//2], cmap="gray")
        plt.title(f"Final Config (mid KT)")
        plt.axis(False)

        plt.subplot(1, 3, 3)
        plt.imshow(self.final[-1], cmap="gray")
        plt.title(f"Final Config (high KT)")
        plt.axis(False)

        plt.show()


def parse_args():
    parser = argparse.ArgumentParser(description="Monte Carlo Spin Lattice Simulation")

    parser.add_argument("--iters", type=int, default=2000,
                        help="Number of Monte Carlo steps (default: 2000)")
    parser.add_argument("--a", type=float, nargs=3, default=[0.1, 0.9, 9],
                        metavar=('A_MIN','A_MAX','A_NUM'),
                        help="Range for J: min max num_points (default: 0.1 0.9 9)")
    parser.add_argument("--b", type=float, nargs=3, default=[0.5, 3.0, 100],
                        metavar=('B_MIN','B_MAX','B_NUM'),
                        help="Range for KT: min max num_points (default: 0.5 3.0 100)")
    parser.add_argument("--N", type=int, default=5,
                        help="Spin lattice grid size (NxN)")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    sim = Simulator(iters=args.iters, a=args.a, b=args.b, N=args.N)
    sim.MC()
    sim.plot()
