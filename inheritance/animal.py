class Animal():
    def __init__(self, paws_number):
        self.paws_number = paws_number


class Mammal(Animal):
    def __init__(self, fur_color, **kw):
        super().__init__(**kw)
        self.fur_color = fur_color

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'

class Bird(Animal):
    def __init__(self, beak_color, **kw):
        super().__init__(**kw)
        self.beak_color = beak_color

class Cat(Mammal):
    pass