"""
*What is this pattern about?
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.

*TL;DR
Enables selecting an algorithm at runtime.
"""
from abc import ABC, abstractmethod
from zope.interface import Interface, implementer


class Duck(ABC):
    fly_behavior = None
    quack_behavior = None

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    @staticmethod
    def swim():
        print('All ducks float, even decoys!')

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior


class IFlyBehavior(Interface):
    """Any flying thing"""
    def fly():
        """Make a fly"""


@implementer(IFlyBehavior)
class FlyWithWinds(object):

    @staticmethod
    def fly():
        print('I’m flying!!')


@implementer(IFlyBehavior)
class FlyNoWay(object):

    @staticmethod
    def fly():
        print('I can’t fly')


@implementer(IFlyBehavior)
class FlyRocketPowered(object):

    @staticmethod
    def fly():
        print('I’m flying with a rocket!')


class IQuackBehavior(Interface):
    """Any quack thing"""
    def quack():
        """Make a quack """


@implementer(IQuackBehavior)
class Quack(object):

    @staticmethod
    def quack():
        print('Quack')


@implementer(IQuackBehavior)
class MuteQuack(object):

    @staticmethod
    def quack():
        print('<< Silence >>')


@implementer(IQuackBehavior)
class Squeak(object):

    @staticmethod
    def quack():
        print('Squeak')


class MallardDuck(Duck):
    fly_behavior = FlyWithWinds
    quack_behavior = Quack

    def display(self):
        print('I’m a real Mallard duck')


class ModelDuck(Duck):
    fly_behavior = FlyNoWay
    quack_behavior = Quack

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
    >>> model.set_fly_behavior(FlyRocketPowered)
    >>> model.perform_fly()
    I’m flying with a rocket!
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
