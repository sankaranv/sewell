import networkx as nx
import torch

class DAG(nx.DiGraph):

    def __init__(self, incoming_graph_data=None):
        
        super(DAG, self).__init__(incoming_graph_data)

        # Check if incoming graph data results in an acyclic graph
        try:
            cycles = list(nx.find_cycle(self))
        except nx.NetworkXNoCycle:
            pass
        else:
            raise ValueError(f"Cycles were found in the given graph: {cycles}")

        self.observed_vars = set()
        self.latent_vars = set()
        self.data = {}

    def add_node(self, node_name, is_observed=True, node_data=None, **kwargs):

        # Check if the node is observed or latent
        if not is_observed:
            self.latent_vars.add(node_name)

        # Nodes can hold data
        self.data[node_name] = node_data

        # Add the node to the graph
        super(DAG, self).add_node(node_name, **kwargs)

    def add_edge(self, u, v, **kwargs):
        return super().add_edge(u, v, **kwargs)

    def get_parents(self, node_name):
        return list(self.predecessors(node_name))

    def get_children(self, node_name):
        return list(self.successors(node_name))

    def get_ancestors(self, node_name):
        return list(nx.ancestors(self, node_name))

    def get_descendants(self, node_name):
        return list(nx.descendants(self, node_name))

    def is_d_separated(self, x, y, z):
        # Check if x and y are d-separated given z
        return nx.d_separated(self, x, y, z)

    def is_d_connected(self, x, y, z):
        # Check if x and y are d-connected given z
        return not nx.d_separated(self, x, y, z)

    def get_all_independencies(self, include_latents=False):

        nodes = set(self.nodes())
        if not include_latents:
            nodes = nodes - self.latent_vars

    def do(self, nodes, data: dict, in_place=False):

        # Applies the do operator for one node and returns a new DAG
        if not set(nodes).issubset(set(self.nodes())):
            raise ValueError(f"Nodes {set(nodes) - set(self.nodes)} not in graph")

        dag = self if in_place else self.copy()

        for node in nodes:
            parents = self.get_parents(node)
            for parent in parents:
                dag.remove_edge(parent, node)
            if isinstance(nodes, list):
                dag.data[node] = data[node]
            else:
                dag.data[node] = data                
        return dag

    def do_(self, nodes, data: dict):

        # Applies the do operator in-place
        self.do(nodes, data, in_place=True)