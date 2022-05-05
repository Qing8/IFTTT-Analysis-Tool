from PhysicalDevice import PhysicalDevice
from Slack import *
from Email import * 
from Edge import * 
from Door import *
import networkx as nx
G = nx.MultiDiGraph()


def add_nodes():

    slack = Slack()
    email_top = Email()

    G.add_node(slack)
    G.add_node(email_top)
    email_slack_edge = Edge(email_top, slack)
    G.add_edge(email_top, slack, email_slack_edge)
    
    detect_info_leak(slack)

    door = Door()
    email_bottom = Email()
    G.add_node(door)
    G.add_node(email_bottom)
    door_email_edge = Edge(door, email_bottom)
    G.add_edge(door, email_bottom, door_email_edge)

    email_edge = Edge(email_bottom, email_top)
    G.add_edge(email_bottom, email_top, email_edge)

    # email_edge2 = Edge(email_top, email_bottom)
    # G.add_edge(email_top, email_bottom, email_edge2)

    detect_info_leak(slack)



def detect_info_leak(node):
    print("\n================ secrecy leak detection ================")
    all_share_list = set()
    info_acc = set()

    for node1, node2, edge, _ in nx.edge_dfs(G, node, orientation="reverse"):
        for share_people in node2.share_list:
            all_share_list.add(share_people.lower())
        
        info_acc.add(edge.edge_info)
        
        if (len(all_share_list) > len(node2.share_list)):
            print("Applet: [{} -> {}] leaks [{}] directly to {}, but [{}] are also potential viewers.\n".format(\
                    node1.node_name, node2.node_name, \
                        edge.edge_info, node2.share_list, all_share_list-set([name.lower() for name in node2.share_list])))
        else:
            print("Applet: [{} -> {}] leaks [{}] directly to {}\n".\
                format(node1.node_name, node2.node_name, edge.edge_info, node2.share_list))
    print("At node {}, information {} can be seen by {}.\n".format(node.node_name, info_acc, node.share_list))

add_nodes()
