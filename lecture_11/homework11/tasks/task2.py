"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from abc import ABC
from typing import Type


class Order:
    """Defines the interface for clients. It helps to get final price counting discount
        system.

    Order accepts a Discount through the constructor, but also possible to change
        Discount at runtime.

    """

    def __init__(self, price: float, discount: Type["Discount"]) -> None:
        """Initialised class instance.

        Args:
            price: of order;
            discount: current Discount class.

        """

        self.price = price
        self._discount = discount

    @property
    def discount(self) -> Type["Discount"]:
        """Reference to the current Discount class.

        Returns:
            current Discount class.

        """

        return self._discount

    @discount.setter
    def discount(self, discount: Type["Discount"]) -> None:
        """Allows replacing a Discount object at runtime.

        Args:
            discount: new Discount class.

        """

        self._discount = discount

    def get_final_price(self, price: float = None) -> float:
        """Gets a final price from given price of order and Discount.

        price argument allows to change Order price at any time.

        Args:
            price: current price of order. Defaults to price, given during Order
            initialisation.

        Returns:
            final price.

        """

        return self._discount.count_final_price(self, price)


class Discount(ABC):
    """Declares interface which common for all successors.

    The Order uses this interface to get final price defined by concrete
    discount class.

    Raises:
        NotImplementedError: if any of successors don't have required class attribute.

    Returns:
        final price.

    """

    discount = 0.0

    def __init_subclass__(cls):
        """Checks if subclasses have required attribute.

        Raises:
            NotImplementedError: if any of successors don't have required class
            attribute.

        """

        required_attribute = "discount"
        if not hasattr(cls, required_attribute):
            raise NotImplementedError(
                f"Class {cls} lacks required `{required_attribute}` class attribute"
            )

    @classmethod
    def count_final_price(cls, order: Order, price: float = None) -> float:
        """Declares the part of interface which counts final price.

        Args:
            order: Order object;
            price: price of counting. Defaults to price given during initialisation.

        Returns:
            final price.

        """

        if price:
            return price - price * cls.discount
        return order.price - order.price * cls.discount


class MorningDiscount(Discount):
    """Keeps size of discount and counts final price.

    Interface has been declared at Discount class.

    Attribute:
        discount: size of discount.

    """

    discount = 0.5


class ElderDiscount(Discount):
    """Keeps size of discount and counts final price.

    Interface has been declared at Discount class.

    Attribute:
        discount: size of discount.

    """

    discount = 0.9
