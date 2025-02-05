# CECS-427-Assignment-Graphs
## Objective:

The objective of this assignment is to implement Erdős-Rényi random graphs. You will create a program in Python with NetworkX and Matplotlib that can generate such graphs, store them in a file, read graphs from files, compute all shortest paths from a specified node using graph algorithms, and visualize the graph along with its shortest paths.

## Requirement

This is the command to execute the Python script graph.py located in the current directory and either reads the file graph_file.gml or creates a random graph. Here, graph_file.gml or the created graph is the graph that will be used for the analysis and the format is Graph Modelling Language (.gml), which describes the graph's structure with attributes. The program should read the attributes of the nodes and edges in the file.

The assignment requires that you create the Python program that runs in a terminal. The program accepts optional parameters. The command to execute the Python is shown in the following line:

```bash
python ./graph.py --input graph_file.gml --create_random_graph n c --plot --BFS a --output out_graph_file.gml
```

## Description of Parameters
The script graph.py must be located in the current directory. Ensure robust file handling mechanisms such as error checking, file existence validation, and appropriate error messages.

```bash
--input graph_file.gml
```

Specifies the input file (graph_file.gml) which describes the graph's structure with attributes from which to read the graph data. This parameter is required to provide the initial graph data for analysis or modification.

```bash
--create_random_graph n c
```

Indicates that a new random graph should be created. This parameter overrides the use of the provided input file and generates a graph based on the subsequent parameters (--nodes and --constant). Relabel the nodes with strings, i.e., the node of node 0 is "0", 1 is "1" and so on. The parameter n defines the number of nodes (n) to be included in the randomly generated graph and the parameter c provides a constant that influences the generation of the random graph. The probability is obtained with the formula (c ln n) / n where n is the number of nodes. This parameter might be used to control properties like edge probability, graph density, or other characteristics of the generated graph.

```bash
--BFS a
```

Specifies a node (a) to compute all the shortest paths (BFS). This parameter, when used, will calculate and display the shortest path distances involving the specified node. It could be useful for analyzing graph properties related to connectivity and path lengths.

```bash
--plot
```

Requests that the graph be plotted. This parameter triggers the visualization of the graph, which can include plotting nodes, edges

```bash
--output out_graph_file.gml
```

Defines the file (out_graph_file.gml) where the resulting graph should be saved. This parameter is used to save the modified or newly created graph to a specified file in Graph Modelling Language (.gml), format.

Examples:

```python
python ./graph.py --create_random_graph 100 1.1 --output out_graph_file.gml
```
This command generates an Erdős-Rényi graph with 100 nodes and an edge probability of (1.1 ln 100) / 100, storing the graph in graph_file.adj_list.

```python
python ./basic_graph.py --input graph_file.gml --BFS 1 --plot
```
This command reads the graph stored in graph_file.gml, computes all the shortest paths (BFS) from 1 to each other node, and plots the graph highlighting the shortest paths.

## Evaluation:
Your implementation will be evaluated based on correctness, efficiency, clarity of code, and the quality of graph visualization. Ensure your program gracefully handles edge cases such as empty graphs, non-existent files, and invalid inputs.

A case of use (program) will be used to evaluate the program. You won't receive any points if it does not follow the instructions.

## Submission:
Submit your source code files along with a README.md file detailing instructions on how to use your program.
