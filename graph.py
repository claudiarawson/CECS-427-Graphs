import argparse
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
import math

# Argument parser using argparse to handle command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description = "Erdos-Renyi Graph Generator and Analyser")
    parser.add_argument("--input", type = str, help = "Input  graph file in .gml format")
    parser.add_argument("--create_random_graph", nargs = 2, type = float, metavar = ("n", "c"), help = "Create an Erdos-Renyi random graph")
    parser.add_argument("--BFS", type = str, help = "Compute shortest paths from a specified node using BFS")
    parser.add_argument("--output", type = str, help = "Output file to save the graph in .gml format")

    return parser.parse_args()

# If input file is given, graph is loaded from .gml
def read_graph(file_name):
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' does not exist.")
        exit(1)
    return nx.read_gml(file_name)

# Otherwise, create a random Erdos-Renyi Graph
def create_random_graph(n, c):
    probability = (c * math.log(n)) / n
    G = nx.erdos_renyi_graph(n, probability)
    G = nx.relabel_nodes(G, {i: str(i) for i in G.nodes()})
    return G

# Find shortest path using Breadth First Search
def compute_shortest_path(G, start_node):
    if start_node not in G:
        print(f"Error: Node '{start_node}' not found in the graph.")
        exit(1)
    
    paths = nx.single_source_shortest_path(G, start_node)
    for target, path in paths.items():
        print(f"Shortest path from {start_node} to {target}: {path}")
    
    return paths

# Using matplotlib to plot the graph and visualise the data
def plot_graph(G, path = None):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)  # Positioning for visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)

    if path:
        # Highlight BFS paths
        for path in path.values():
            edges = list(zip(path, path[1:]))  # Create edges from BFS paths
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    
    plt.show()

# Save graph into output file
def save_graph(G, output):
    return

