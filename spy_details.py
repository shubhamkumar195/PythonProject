from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Shubham', 'Mr.', 24, 3.5)

friend_one = Spy('Ambuj', 'Mr.', 39, 3.9)
friend_two = Spy('Ballia', 'Mr.', 29, 4.1)
friend_three = Spy('Timmy', 'Mrs.', 45, 5.0)


friends = [friend_one, friend_two, friend_three]