class Event:
    def __init__(self):
        self.subscribers = []
    def subscribe(self,function):
        self.subscribers.append(function)
    def notify(self, data):
        for fn in self.subscribers:
            fn(data)

def send_email(body):
    print(f"I am {body}!")

event = Event()

event.subscribe(send_email)

event.notify("Message")