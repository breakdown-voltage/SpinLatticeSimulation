# SpinLatticeSimulation
SpinLatticeSimulation is a comprehensive Monte Carlo simulation tool for studying spin lattices. This repository implements Monte Carlo methods to simulate and analyze the behavior of spin systems, providing insights into phase transitions, magnetic properties, and lattice dynamics.

## Files
- [main.py](main.py) — entry point and CLI; contains the [`Simulator`](main.py) class.
- [helpers.py](helpers.py) — lattice utilities (e.g. [`createLattice`](helpers.py), [`calc_energy`](helpers.py), [`Magnetisation`](helpers.py), [`f`](helpers.py)).
- [Spin_Lattice_Simulation.ipynb](Spin_Lattice_Simulation.ipynb) — example notebook with plots.
- [README.md](README.md) — this file.

## Model (brief)

- Nearest-neighbor energy: `E = -J Σ_<i,j> s_i s_j`
- Magnetization: `M = (1/N^2) Σ_i,j s_ij`
- Metropolis acceptance (default, configurable in [helpers.py](helpers.py)): `P = exp(-ΔE / K)`

## Usage

Install dependencies:
```sh
pip install numpy matplotlib tqdm
```

Run with custom parameters:
```sh
python main.py --iters 2000 --a 0.1 0.9 9 --b 0.5 3.0 100 --N 5
```
- `--a` and `--b` are passed as `[min max num]` and converted to ranges inside [`Simulator`](main.py).

## Notes
- The design is modular: change acceptance behaviour in [`f`](helpers.py) or sweep parameter ranges via the CLI in [`main.py`](main.py).
- Use the notebook [`Spin_Lattice_Simulation.ipynb`](Spin_Lattice_Simulation.ipynb) for interactive exploration.

## Results
These are the results obtained by running the algorithm for a 5x5 2-Dimensional lattice with random spins.
### Magnetization vs. KT:

As temperature (KT) increases, the average magnetization decreases, indicating a phase transition from an ordered to a disordered state.
Higher interaction strengths (J) lead to greater magnetization, even at higher temperatures.
### Spin Configurations:
Initial and final spin configurations reveal the system's transition dynamics.
At low KT, spins align more uniformly, while at high KT, spins appear random.
### Visualization
**Magnetization vs. KT**: A grid of plots showing the dependence of magnetization on temperature for various interaction strengths.

![image](https://github.com/user-attachments/assets/a5212444-d717-475a-8f79-5ec04c8167e7)
**Spin Configurations**: Examples of initial and final lattice states for selected parameters.

![image](https://github.com/user-attachments/assets/9aa2a215-8cd0-4c5e-9d8f-58e8ffa409ca)

The panels above show the evolution of the 2D spin lattice for \( J = 0.9 \):

- **Left:** Random initial spin configuration.  
- **Middle:** Final configuration at low temperature (\( KT = 0.5 \)) — spins align uniformly, forming an ordered **ferromagnetic** state.  
- **Right:** Final configuration at high temperature (\( KT = 3 \)) — thermal agitation randomizes spins, producing a **paramagnetic** (disordered) state.  

These snapshots visually demonstrate the **phase transition** from order to disorder as temperature increases.
