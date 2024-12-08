# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx

# Initialize the graph
G = nx.DiGraph()

# Define nodes with adjusted positions
nodes = {
    # Central nodes (nodes with maximum connections)
    "Inflammation": (0, 0),
    "Macrophages (M1)": (-5, 2),
    "Myofibroblasts": (5, 2),

    # Left side nodes
    "Epithelial Cells": (-10, 4),
    "Monocytes": (-10, 2),
    "Macrophages (M2)": (-5, -2),

    # Right side nodes
    "Fibrosis": (5, -4),
    "ECM": (5, -2),

    # Bottom nodes
    "Efferocytosis": (-5, -4),

    # Nodes to be represented as stars and colored orange
    "SIRPa": (0, -2),
    "QPCTL": (2, 0),
    "pE-CD47": (2, -2),
    "CD47": (2, -4),

    # Cytokines and Chemokines
    "TNF-α": (-5, 4),
    "IL-6": (-5, 6),
    "TGF-β": (5, 4),

    # Proteases and Inhibitors
    "Proteases": (-2, -4),
    "MMPs": (2, -6),
    "TIMPs": (2, -8),

    # Nodes related to the hypothesis
    "QPCTL Inhibitors": (0, 2),
    "Overactivated Macrophages": (-5, 0),
}

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define edges with interactions
edges = [
    # Injury leads to inflammation
    ("Epithelial Cells", "Inflammation", {"style": "solid", "color": "black"}),

    # Inflammation recruits monocytes
    ("Inflammation", "Monocytes", {"style": "solid", "color": "black"}),

    # Monocytes differentiate into macrophages
    ("Monocytes", "Macrophages (M1)", {"style": "solid", "color": "black"}),
    ("Monocytes", "Macrophages (M2)", {"style": "solid", "color": "black"}),

    # Macrophages secrete cytokines
    ("Macrophages (M1)", "TNF-α", {"style": "solid", "color": "black"}),
    ("Macrophages (M1)", "IL-6", {"style": "solid", "color": "black"}),

    # TNF-α and IL-6 promote inflammation
    ("TNF-α", "Inflammation", {"style": "solid", "color": "black"}),
    ("IL-6", "Inflammation", {"style": "solid", "color": "black"}),

    # Inflammation activates myofibroblasts
    ("Inflammation", "Myofibroblasts", {"style": "solid", "color": "black"}),

    # Myofibroblasts produce ECM
    ("Myofibroblasts", "ECM", {"style": "solid", "color": "black"}),

    # MMPs degrade ECM
    ("MMPs", "ECM", {"style": "dashed", "color": "red"}),

    # ECM contributes to fibrosis
    ("ECM", "Fibrosis", {"style": "solid", "color": "black"}),

    # Macrophages perform efferocytosis
    ("Macrophages (M1)", "Efferocytosis", {"style": "solid", "color": "black"}),
    ("Macrophages (M2)", "Efferocytosis", {"style": "solid", "color": "black"}),

    # Efferocytosis reduces inflammation
    ("Efferocytosis", "Inflammation", {"style": "dashed", "color": "red"}),

    # QPCTL catalyzes pE-CD47 formation
    ("QPCTL", "pE-CD47", {"style": "solid", "color": "black"}),
    ("CD47", "pE-CD47", {"style": "solid", "color": "black"}),

    # pE-CD47 binds SIRPa
    ("pE-CD47", "SIRPa", {"style": "solid", "color": "black"}),

    # SIRPa inhibits macrophage phagocytosis
    ("SIRPa", "Macrophages (M1)", {"style": "dashed", "color": "red"}),
    ("SIRPa", "Macrophages (M2)", {"style": "dashed", "color": "red"}),

    # Macrophages secrete MMPs
    ("Macrophages (M1)", "MMPs", {"style": "solid", "color": "black"}),

    # TIMPs inhibit MMPs
    ("TIMPs", "MMPs", {"style": "dashed", "color": "red"}),

    # Myofibroblasts secrete TIMPs
    ("Myofibroblasts", "TIMPs", {"style": "solid", "color": "black"}),

    # Proteases degrade SIRPa
    ("Proteases", "SIRPa", {"style": "solid", "color": "black"}),

    # Macrophages secrete proteases
    ("Macrophages (M1)", "Proteases", {"style": "solid", "color": "black"}),

    # TGF-β promotes myofibroblast activation
    ("TGF-β", "Myofibroblasts", {"style": "solid", "color": "black"}),

    # Myofibroblasts secrete TGF-β
    ("Myofibroblasts", "TGF-β", {"style": "solid", "color": "black"}),

    # Hypothesis-related interactions
    # High concentrations of QPCTL inhibitors lead to overactivation of macrophages
    ("QPCTL Inhibitors", "Overactivated Macrophages", {"style": "solid", "color": "black"}),

    # Overactivated macrophages secrete excess TNF-α and IL-6
    ("Overactivated Macrophages", "TNF-α", {"style": "solid", "color": "black"}),
    ("Overactivated Macrophages", "IL-6", {"style": "solid", "color": "black"}),

    # Excess TNF-α and IL-6 drive increased inflammation
    ("TNF-α", "Inflammation", {"style": "solid", "color": "black"}),
    ("IL-6", "Inflammation", {"style": "solid", "color": "black"}),
]

# Add edges to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], **edge[2])

# Define edge styles and colors
edge_styles = {}
edge_colors = {}
for u, v, data in G.edges(data=True):
    edge_styles[(u, v)] = data.get('style', 'solid')
    edge_colors[(u, v)] = data.get('color', 'black')

# Set positions
pos = nodes

# Initialize plot
plt.figure(figsize=(24, 18))

# Draw nodes with different shapes and colors

# Nodes with star shape and orange color
star_nodes = ['SIRPa', 'QPCTL', 'pE-CD47', 'CD47']
nx.draw_networkx_nodes(G, pos,
                       nodelist=star_nodes,
                       node_shape='*',
                       node_color='orange',
                       node_size=1000)

# Nodes with rectangle shape
rect_nodes = ['Inflammation', 'Fibrosis', 'Efferocytosis']
nx.draw_networkx_nodes(G, pos,
                       nodelist=rect_nodes,
                       node_shape='s',  # square shape for rectangles
                       node_color='lightblue',
                       node_size=1000)

# Other nodes
other_nodes = list(set(G.nodes()) - set(star_nodes) - set(rect_nodes))
nx.draw_networkx_nodes(G, pos,
                       nodelist=other_nodes,
                       node_shape='o',  # circle shape
                       node_color='lightblue',
                       node_size=1000)

# Draw edges with styles and appropriate arrow styles
for u, v in G.edges():
    style = edge_styles[(u, v)]
    color = edge_colors[(u, v)]
    if style == 'solid':
        arrow_style = '-|>'  # Standard arrow for activation
    elif style == 'dashed':
        arrow_style = '-['   # Bar-headed arrow for inhibition
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
        arrowsize=15,
        connectionstyle='arc3,rad=0.1'
    )

# Draw node labels
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9, font_weight='bold')

# Edge labels are not drawn, as per your previous request

# Add legend manually
from matplotlib.patches import FancyArrowPatch

legend_elements = [
    FancyArrowPatch((0, 0), (1, 0),
                    connectionstyle='arc3,rad=0',
                    arrowstyle='-|>',
                    color='black',
                    mutation_scale=15,
                    lw=2,
                    label='Activation (Upregulation)'),
    FancyArrowPatch((0, 0), (1, 0),
                    connectionstyle='arc3,rad=0',
                    arrowstyle='-[',
                    linestyle='dashed',
                    color='red',
                    mutation_scale=15,
                    lw=2,
                    label='Inhibition (Downregulation)'),
]

plt.legend(handles=legend_elements, loc='upper left', fontsize='medium')

# Set title
plt.title("Comprehensive Interaction Diagram: Pulmonary Fibrosis Pathogenesis", fontsize=14)

# Remove axes
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
