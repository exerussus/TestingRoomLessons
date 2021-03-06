class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


if __name__ == '__main__':
    import copy
    Ilya = Person('Ilya', Address('Bolshaya 100', 'Ryazan', 'Russia'))
    Beth = copy.deepcopy(Ilya)
    Beth.name = 'Beth'
    print('---')
    print('', Ilya, '\n', Beth)

    Beth.address.street_address = 'Novoselov 7'
    print('---')
    print('', Ilya, '\n', Beth)
