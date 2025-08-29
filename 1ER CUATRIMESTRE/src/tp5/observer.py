class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def notify(self, event_id):
        print(f"Emitiendo ID: {event_id}")
        for observer in self.subscribers:
            observer.update(event_id)

class Observer:
    def __init__(self, id_obj):
        self.id_obj = id_obj

    def update(self, event_id):
        if self.id_obj == event_id:
            print(f"Observador {self.id_obj} recibió el ID {event_id}")


pub = Publisher()
ids = ['AB12', 'CD34', 'EF56', 'GH78']
for ident in ids:
    pub.subscribe(Observer(ident))

eventos = ['ZZ99', 'CD34', 'AB12', 'XY00', 'EF56', 'GH78', 'TT11', 'WW22']
for eid in eventos:
    pub.notify(eid)
