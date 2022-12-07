import networkx as nx
import torch

class DAG(nx.DiGraph):

    def __init__(self, incoming_graph_data=None):
        
        super(DAG, self).__init__(incoming_graph_data)
        # Check if incoming graph data results in an acyclic graph
        cycles = list(nx.find_cycle(self))
        assert(len(cycles == 0)), f"Cycles were found in the given graph: {cycles}"

    

