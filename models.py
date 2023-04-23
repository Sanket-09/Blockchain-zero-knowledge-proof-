from datetime import datetime


class Property:

    properties = []

    def __init__(self, name, amount, owner=None):
        self.id = len(self.properties)
        self.name = name
        self.owner = owner
        self.amount = amount
        self.transaction_history = []
        self.properties.append(self)


class Transaction:

    def __init__(self, seller, buyer, property, pos):
        self.buyer = buyer
        self.seller = seller
        self.propertyId = property.id
        self.timestamp = datetime.utcnow().isoformat()
        self.transactionId = str(hash(buyer.username + property.name))
        self.pos = pos
        property.owner = buyer


class User:

    users = []

    def __init__(self, username, password, wealth=1500):
        self.username = username
        self.password = password
        self.wealth = wealth
        self.assets = {}
        self.users.append(self)

    def add_property(self, property):   
        self.wealth -= property.amount
        self.assets[property.id] = property
        property.owner = self

    def remove_property(self, property):
        self.wealth += property.amount
        del self.assets[property.id]

    def get_assets(self):
        for key in self.assets:
            print(str(key) + ':', self.assets[key].name)
