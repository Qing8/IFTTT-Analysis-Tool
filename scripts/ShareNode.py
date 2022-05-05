import abc 

class ShareNode:
    def __init__(self):
        super().__init__()
        self.node_name = self.get_node_name() 
        self.share_list = set()
        self.removed_view_future = False 
        self.newly_view_history = False 
        self.node_type =  self.get_node_type()
        
        self.begin()

    def begin(self):
        self.ask_node_state()
        self.ask_share_list()
        self.print_share_list_summary()
        if len(self.share_list) > 0:
            self.ask_share_policy() 
            self.print_sharing_policy_summary()

    @abc.abstractmethod  
    def ask_node_state(self):
        raise NotImplementedError
        
    def print_share_list_summary(self):
        print("Summary of shared list: \n\t{} could view content of {}\n".format(self.share_list, self.node_name))
    
    def print_sharing_policy_summary(self):
        
        print("Summary of sharing policy: ")
        if self.removed_view_future:
            view_str = ""
        else:
            view_str = " not"
        print("\tremoved person can" + view_str + " view future messages.")

        # if (self.newly_view_history):
        #     view_str = ""
        # else:
        #     view_str = " not"
        # print("\tnewly added person can" + view_str + " view history messages.")

    def get_node_type(self):
        return input("Is this device a trigger or action? [trigger/action]\n> ").lower()

    @abc.abstractmethod
    def get_node_name(self):
        raise NotImplementedError

    def ask_share_policy(self):
        removed_view_future_answer = input("Can removed person view future messages? [Y/n]\n> ").lower()
        self.removed_view_future = (removed_view_future_answer == "y")
        # newly_view_history_answer = input("Can newly joined person view history messages? [Y/n]\n> ").lower()
        # self.newly_view_history = (newly_view_history_answer == "y")

    def add_to_share_list(self, person):
        self.share_list.add(person)

    def remove_from_share_list(self, person):
        if person not in self.share_list:
            return 

        self.share_list.remove(person)

    def ask_share_list(self):
        person = input("Who could view the content of {}? [type 'quit' to exit]\n> ".format(self.node_name))
        while (person != "quit"):
            self.add_to_share_list(person)
            person = input("Who could view the content? [type 'quit' to exit]\n> ")
        