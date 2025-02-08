import argparse
import networkx as nx
import matplotlib.pyplot as plt
import os
import math

# Argument parser using argparse to handle command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description = "Erdos-Renyi Graph Generator and Analyser")
    parser.add_argument("--input", type = str, help = "Input graph file in .gml format")
    parser.add_argument("--create_random_graph", nargs = 2, type = float, metavar = ("n", "c"), help = "Create an Erdos-Renyi random graph")
    parser.add_argument("--BFS", type = str, help = "Compute shortest paths from a specified node using BFS")
    parser.add_argument("--plot", action ="store_true", help ="Plot the graph")
    parser.add_argument("--output", type = str, help = "Output file to save the graph in .gml format")

    return parser.parse_args()

# If input file is given, graph is loaded from .gml
def read_graph(file_name):
    if not os.path.exists(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        exit(1)
    return nx.read_gml(file_name)

# Otherwise, create a random Erdos-Renyi Graph
def create_random_graph(n, c):
    n = int(n)
    if n <= 0:
        print("Error: The number of nodes has to be larger than 0.")
        return None
    probability = (c * math.log(n)) / n
    G = nx.erdos_renyi_graph(n, probability)
    G = nx.relabel_nodes(G, {i: str(i) for i in G.nodes()})
    return G

# Find shortest path using Breadth First Search
def compute_shortest_path(G, start_node):
    if start_node not in G:
        print(f"Error: Node '{start_node}' was not found in the graph.")
        exit(1)
    paths = nx.single_source_shortest_path(G, source = start_node)  
    return paths

# Using matplotlib to plot the graph and visualise the data
def plot_graph(G, start_node = None, title = "Graph"):
    if start_node:
        if start_node not in G:
            print(f"Error: Node {start_node} does not exist in the graph.")
            return
        
        # Performing BFS only to reachable nodes by the user given start node
        bfs_graph = nx.bfs_tree(G, source = start_node)
        G = bfs_graph
        title = f"BFS Tree from Node {start_node}"

    node_colours = ["red" if node == start_node else "lightblue" for node in G.nodes()]

    # Plot the graph (original or BFS subgraph)
    plt.figure(figsize = (8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels = True, node_color = node_colours, edge_color = "gray", node_size = 700, font_size = 12)
    plt.title(title)
    plt.show()

# Save graph into output file
def save_graph(G, output):
    nx.write_gml(G, output)
    print(f"Graph saved to {output}")

def main():
    args = parse_arguments()
    G = None

    if args.input:
        G = read_graph(args.input)
        if G is None:
            return

    if args.create_random_graph:
        n, c = args.create_random_graph
        G = create_random_graph(n, c)
        if G is None:
            return

    if args.output and G:
        save_graph(G, args.output)

    if args.BFS and G:
        shortest_paths = compute_shortest_path(G, args.BFS)
        for node, path in shortest_paths.items():
            print(f"Shortest paths from node {args.BFS}: {path}")
        plot_graph(G, start_node = args.BFS)
    elif args.plot and G:
        plot_graph(G)

if __name__ == "__main__":
    main()