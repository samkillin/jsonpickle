import jsonpickle


class Dog:
    paws = None
    woofs = None

    def __init__(self, paws, woofs):
        self.paws = paws
        self.woofs = woofs

    def get_paws(self):
        return self.paws

    def get_woofs(self):
        return self.woofs

dog = Dog(4, "ALWAYS")
encoded = jsonpickle.encode(dog, unpicklable=True)
print(encoded)

decoded = jsonpickle.decode(encoded, cls=None)
print(decoded)

