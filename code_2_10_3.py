class Birds:
    def __init__(self, type, age):
        self.type = type
        self.age = age

    def can_fly(self):
        print('I can fly.')

    def can_swim(self):
        print('I cannot swim')

    def mammal(self):
        print('I am not mammal.')


class Fish(Birds):
    def can_swim(self):
        print('I can swim.')

    def can_fly(self):
        print('I cannot fly')


class Mammals(Fish):
    def mammal(self):
        print('I am mammal.')


class Predators:
    def eat(self):
        print('I eat meat or fish.')


class Herbivores:
    def eat(self):
        print('I don\'t eat meat or fish.')


class Penguin(Birds, Predators):
    def __init__(self, type, age):
        super().__init__(type, age)
        print('I am penguin.')

    def can_swim(self):
        print('I can swim.')

    def can_fly(self):
        print('I cannot fly.')


class Falcon(Birds, Predators):
    def __init__(self, type, age):
        super().__init__(type, age)
        print('I am falcon.')


class Trout(Fish, Predators):
    def __init__(self, type, age):
        super().__init__(type, age)
        print('I am trout.')


class Whale(Mammals, Herbivores):
    def __init__(self, type, age):
        super().__init__(type, age)
        print('I am whale.')

p = Penguin(type='royal', age='1 year')
p.eat()
p.can_swim()
p.can_fly()
p.mammal()

f = Falcon(type='subniger', age='3 years')
f. eat()
f.can_swim()
f.can_fly()
f.mammal()

t = Trout(type='mykiss', age='2 years')
t.eat()
t.can_swim()
t.can_fly()
t.mammal()

w = Whale(type='mysticeti', age='45 years')
w.eat()
w.can_swim()
w.can_fly()
w.mammal()
