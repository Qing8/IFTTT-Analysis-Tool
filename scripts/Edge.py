class Edge:
    def __init__(self, start_node, end_node):
        self.start_node = start_node 
        self.end_node = end_node 
        self.edge_info = self.get_edge_info()
        

    def get_edge_info(self):
        leaked_info = input("if [{}] is {}, what information will be shared/logged at {}\n> ".format(self.start_node.node_name, self.start_node.node_state.name, self.end_node.node_name))
        return leaked_info
