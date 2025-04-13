from models import Node
import uuid

class NodeManager:
    def __init__(self):
        self.nodes = {}

    def add_node(self, cpu_cores):
        node = Node(cpu_cores)
        self.nodes[node.id] = node
        return node.id

    def get_nodes(self):
        return self.nodes

    def get_node(self, node_id):
        return self.nodes.get(node_id)
