# Overview
This project implements an Erdos-Renyi random graph generator using **NetworkX** and **Matplotlib**. This program will allow users to create a random graph with **n** nodes and edge probability **p**, read and write graphs in **.gml** format, compute **shortest paths** using **BFS**, and help visualise the graph and BFS tree.

# Installation
1. Clone the Repository
```bash
gh repo clone claudiarawson/CECS-427-Assignment-Graphs
```
2. Install Dependencies
```bash
pip install networkx matplotlib
```

# Usage

### Libraries used are:
* networkx
* matplotlib

### Parameters

| **Option**                     | **Description**                                               | **Example**                                      |
|---------------------------------|---------------------------------------------------------------|--------------------------------------------------|
| `--input <file>`                | Reads a graph from a **.gml** file                            | `--input graph_file.gml`                         |
| `--create_random_graph n c`     | Generates an **Erdős-Rényi** graph with `n` nodes and constant `c` | `--create_random_graph 100 1.1`                  |
| `--BFS a`                       | Computes BFS starting from node `a`                           | `--BFS 1`                                        |
| `--plot`                        | Plots the graph                                               | `--plot`                                         |
| `--output <file>`               | Saves the graph to a **.gml** file                             | `--output out_graph_file.gml`                    |

### Procedure
**1. Create an Erdos Renyi Graph and saving it**
```bash
python graph.py --create_random_graph n c --output my_graph.gml
```
Where `n` represents the node, and `c` represents the constant. See parameters.

**2. Load the created graph and compute its Breadth First Search (BFS)**
```bash
python graph.py --input my_graph.gml --BFS x --plot
```
Where `x` is the node that BFS is starting from, and the relationship between `x` and `n` is `0 ≤ x = n`. Any value of `x` outside of the range will generate an error.

### Have a good time coding! :)