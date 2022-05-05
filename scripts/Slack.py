from ShareNode import * 
from EndToEnd import * 
from enum import Enum 

class SlackStateEnum(Enum):
    RECEIVE_MESSAGE = 1
    SEND_MESSAGE = 2

class Slack(ShareNode, EndToEnd):
    def __init__(self):
        super().__init__()
               

    def get_account_id(self):
        print("================ Setting up Slack ================")
        an = input("What is the slack account? \n> ")
        return an 
        

    def get_channel_name(self):
        cn = input("What is the channel name? \n> ")
        return cn 

    def get_node_name(self):
        self.account_id = self.get_account_id()
        self.channel_name = self.get_channel_name() 
        node_name =  "[{} at {}]".format(self.account_id, self.channel_name)
        print("the node name is {}".format(node_name))
        return node_name
    
    def ask_add_send_to(self):
        ask_string = "Who would you like to send to? (`quit` to stop entering)\n> "
        person = input(ask_string).lower()
        while (person != 'quit'):
            self.add_sent_to(person)
            person = input(ask_string).lower() 
        print("{} will receive from {}".format(self.node_name, self.receive_from))
        
    def ask_add_receive_from(self):
        person = input("Who would you like to receive from? (`quit` to stop entering)\n> ").lower()
        while (person != 'quit'):
            self.add_receive_from(person)
            person = input("Who would you like to receive from? (`quit` to stop entering)\n> ").lower() 
        print("{} will receive from {}".format(self.node_name, self.receive_from))

    def ask_node_state(self):
        print("================ Set the Slack node state ================")
        print("{} has the following state:".format(self.node_name))
        for s in SlackStateEnum:
            print(s.name)
        state = input("please choose one from above: \n> ")
        self.node_state = SlackStateEnum[state]
        print("Summary: You have set Node {} to state [{}].".format(self.node_name, self.node_state))
        if (self.node_state == SlackStateEnum.RECEIVE_MESSAGE):
            self.ask_add_receive_from()
        elif self.node_state == SlackStateEnum.SEND_MESSAGE:
            self.ask_add_send_to() 
        
if __name__ == '__main__':
    slack1 = Slack()
