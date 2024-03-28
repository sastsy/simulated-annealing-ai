# Simulated Annealing Algorithm for Shortest Hamilton Cycle

This repository contains an implementation of the simulated annealing algorithm to find the shortest Hamilton cycle in a graph.

## Contents

- [Overview](#overview)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

Simulated annealing is a probabilistic optimization technique used to find approximate solutions to optimization problems. In this implementation, the algorithm is applied to find the shortest Hamilton cycle in a given directed graph. A Hamilton cycle is a cycle that visits each vertex exactly once and returns to the starting vertex.

The modification introduced in this implementation involves dynamic cooling rates. Instead of using a fixed cooling rate, the cooling rate decreases over time. This change aims to allow for more exploration in the early stages of the algorithm and more exploitation in the later stages.


## Usage

To use the simulated annealing algorithm:

1. Ensure you have Python installed on your system.
2. Install the required dependencies listed in the [Dependencies](#dependencies) section.
3. Run the `GUI.py` file.
4. Click on the canvas to add vertices.
5. Click on the "Add Weighted Edge" button to add edges between vertices.
6. Once the graph is constructed, click on the "Calculate Cycle" button to find the shortest Hamilton cycle.

## File Structure

- `annealing.py`: Contains the implementation of the simulated annealing algorithm.
- `GUI.py`: Implements a graphical user interface for visualizing graphs and interacting with the algorithm.
  
## Dependencies

- `networkx`: For handling graphs and calculating the Hamilton cycle cost.
- `tkinter`: For creating the graphical user interface.
- `matplotlib`: For plotting the graph visualization.
- `numpy`: For numerical calculations.
  
You can install the dependencies using pip:

```bash
pip install networkx matplotlib numpy
```