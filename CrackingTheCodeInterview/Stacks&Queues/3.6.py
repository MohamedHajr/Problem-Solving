class Animal:
    def __init__(self, name, animalType, id, next=None):
        self.name = name
        self.type = animalType
        self.id = id
        self.next = next


class Shelter:
    def __init__(self):
        self.dogsHead = None
        self.dogsTail = None
        self.catsHead = None
        self.catsTail = None
        self. id = 0

    def add(self, animal, head, tail):
        if not head:
            head = animal
            tail = animal
        else:
            tail.next = animal
            tail = animal
        return head, tail

    def enqueue(self, name, animalType):
        animal = Animal(name, animalType, self.id)
        self.id += 1
        if animalType == 'dog':
            self.dogsHead, self.dogsTail = self.add(
                animal, self.dogsHead, self.dogsTail)
        else:
            self.catsHead, self.catsTail = self.add(
                animal, self.catsHead, self.catsTail)

    def dequeueAny(self):
        if self.dogsHead.id > self.catsHead.id:
            return self.dequeueCat()
        else:
            return self.dequeueDog()

    def dequeueCat(self):
        current = self.catsHead
        if self.catsHead == self.catsTail:
            self.catsTail = self.catsTail.next
        self.catsHead = self.catsHead.next
        return current

    def dequeueDog(self):
        current = self.dogsHead
        if self.dogsHead == self.dogsTail:
            self.dogsTail = self.dogsTail.next
        self.dogsHead = self.dogsHead.next
        return current
