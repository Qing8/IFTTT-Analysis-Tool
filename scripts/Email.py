from __future__ import annotations
from enum import Enum
from EndToEnd import EVERYONE, EndToEnd
from ShareNode import ShareNode

class EmailStateEnum(Enum):
    RECEIVE_EMAIL = 1
    SEND_EMAIL = 2
    
class Email(ShareNode, EndToEnd):
    def __init__(self):
        super().__init__()

    def set_node_state(self):
        print("set_node_state")

    def get_node_name(self):
        print("================ setting up email node ================")
        self.email_account = input("what is your email account?\n> ")
        return "[{}]".format(self.email_account)

    def ask_node_state(self):
        print("================ Set the email node state ================")
        print("{} has the following state:".format(self.node_name))
        for s in EmailStateEnum:
            print(s.name)
        state = input("please choose one from above: \n> ")
        self.node_state = EmailStateEnum[state]
        print("Summary: You have set Node {} to state [{}].".format(self.node_name, self.node_state))
        if (self.node_state == EmailStateEnum.RECEIVE_EMAIL):
            self.ask_add_receive_from()
        elif self.node_state == EmailStateEnum.SEND_EMAIL:
            self.ask_add_send_to() 
    
    def ask_add_send_to(self):
        ask_string = "Who would you like to send to? (`quit` to stop entering)\n> "
        person = input(ask_string).lower()
        while (person != 'quit'):
            self.add_sent_to(person)
            person = input(ask_string).lower() 
        print("{} will receive from {}".format(self.node_name, self.send_to))
        
    def ask_add_receive_from(self):
        person = input("Who would you like to receive from? (`quit` to stop entering)\n> ").lower()
        while (person != 'quit'):
            self.add_receive_from(person)
            person = input("Who would you like to receive from? (`quit` to stop entering)\n> ").lower() 
        print("{} will receive from {}".format(self.node_name, self.receive_from))

        
if __name__ == '__main__':
    email = Email()