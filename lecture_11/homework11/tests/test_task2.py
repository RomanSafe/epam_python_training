from lecture_11.homework11.tasks.task2 import ElderDiscount, MorningDiscount, Order


def test_order_1():
    order = Order(100, MorningDiscount)

    assert order.get_final_price() == 50


def test_order_change_discount_and_price():
    order = Order(100, MorningDiscount)
    order.discount = ElderDiscount

    assert order.discount == ElderDiscount
    assert order.get_final_price() == 10
    assert order.get_final_price(300) == 30
