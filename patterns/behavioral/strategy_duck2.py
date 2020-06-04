"""
*What is this pattern about?
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.

*TL;DR
Enables selecting an algorithm at runtime.
"""


def fly_with_winds(self):
    return 'I’m flying!!'


def fly_no_way(self):
    return 'I can’t fly'


def fly_rocket_powered(self):
    return 'I’m flying with a rocket!'


def quack(self):
    return 'Quack'


def mute_quack(self):
    return '<< Silence >>'


def squeak(self):
    return 'Squeak'


class Duck:
    def __init__(self, fly_behavior=None, quack_behavior=None):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        if self.fly_behavior:
            result = self.fly_behavior(self)
        else:
            result = '<< >>'
        print(result)

    def perform_quack(self):
        if self.quack_behavior:
            result = self.quack_behavior(self)
        else:
            result = '<< >>'
        print(result)

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def display(self):
        print('I’m a duck')


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(fly_with_winds, quack)

    def display(self):
        print('I’m a real Mallard duck')


class ModelDuck(Duck):
    def __init__(self):
        super().__init__(fly_no_way, quack)

    def display(self):
        print('I’m a Model duck')


def main():
    """
    >>> MallardDuck().perform_quack()
    Quack
    >>> MallardDuck().perform_fly()
    I’m flying!!
    >>> ModelDuck().perform_quack()
    Quack
    >>> model = ModelDuck()
    >>> model.perform_fly()
    I can’t fly
    >>> model.set_fly_behavior(fly_rocket_powered)
    >>> model.perform_fly()
    I’m flying with a rocket!
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
