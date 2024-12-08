# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx

# Initialize the graph
G = nx.DiGraph()

# Define nodes with positions for clear visualization
nodes = {
    "High Concentration\nof QPCTL Inhibitors": (0, 3),
    "QPCTL": (0, 1),
    "Reduced CD47\nModification": (0, -1),
    "Impaired CD47-SIRPα\nInteraction": (0, -3),
    "Macrophage\nOveractivation": (0, -5),
    "Excess TNF-α and IL-6": (-2, -7),
    "Increased\nInflammation": (0, -9),
    "Exacerbation of\nPulmonary Fibrosis": (0, -11),
}

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define edges with interactions
edges = [
    ("High Concentration\nof QPCTL Inhibitors", "QPCTL", {"style": "dashed", "color": "red"}),
    ("QPCTL", "Reduced CD47\nModification", {"style": "solid", "color": "black"}),
    ("Reduced CD47\nModification", "Impaired CD47-SIRPα\nInteraction", {"style": "solid", "color": "black"}),
    ("Impaired CD47-SIRPα\nInteraction", "Macrophage\nOveractivation", {"style": "solid", "color": "black"}),
    ("Macrophage\nOveractivation", "Excess TNF-α and IL-6", {"style": "solid", "color": "black"}),
    ("Excess TNF-α and IL-6", "Increased\nInflammation", {"style": "solid", "color": "black"}),
    ("Increased\nInflammation", "Exacerbation of\nPulmonary Fibrosis", {"style": "solid", "color": "black"}),
]

# Add edges to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], **edge[2])

# Set positions
pos = nodes

# Initialize plot
plt.figure(figsize=(10, 12))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue', node_shape='s')

# Draw edges with styles and appropriate arrow styles
for u, v in G.edges():
    style = G[u][v]['style']
    color = G[u][v]['color']
    if style == 'solid':
        arrow_style = '-|>'
    elif style == 'dashed':
        arrow_style = '-['
    else:
        arrow_style = '-|>'
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=[(u, v)],
        style=style,
        edge_color=color,
        arrows=True,
        arrowstyle=arrow_style,
        arrowsize=20,
        connectionstyle='arc3,rad=0.0'
    )

# Draw node labels
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight='bold')

# Remove axes
plt.axis('off')

# Set title
plt.title("Effect Diagram: High QPCTL Inhibitor Concentration Leading to Increased Inflammation", fontsize=14)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
