import argparse
import networkx as nx
import matplotlib.pyplot as plt
import os

# Argument parser using argparse to handle command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(descriptopn = "Erdos-Renyi Graph Generator and Analyser")
    parser.add_argument("--input", type = str, help = "Input  graph file in .gml format")
    parser.add_argument("--create_random_graph", nargs = 2, type = float, metavar = ("n", "c"), help = "Create an Erdos-Renyi random graph")
    parser.add_argument("--BFS", type = str, help = "Compute shortest paths from a specified node using BFS")
    parser.add_argument("--output", type = str, help = "Output file to save the graph in .gml format")

    return parser.parse_args()

# Load or create a graph

# If input file is given, graph is loaded from .gml
def load(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        exit(1)
    return nx.read_gml(file_path)

# Otherwise, create a random Erdos-Renyi Graph
def rcreate(n, c):
    return

# Find shortest path using Breadth First Search
def bfs(G, start_node):
    return

# Using matplotlib to plot the graph and visualise the data
def plot(G, bfs_paths = None):
    return

# Save graph into output file
def save(G, output):
    return

