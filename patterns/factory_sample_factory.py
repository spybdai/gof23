"""
factory patterns:
* sample factory


It's similar as strategy patter more or less.
use another 'interface' to do something.
"""


class PizzaStore(object):

    def __init__(self, pizza_factory):
        self.pizza_factory = pizza_factory

    def order_pizza(self, pizza_type):

        pizza = self.pizza_factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class Pizza(object):

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class CheesePizza(Pizza):
    pass


class VeggiePizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class SampleFactory(object):

    def create_pizza(self, pizza_type):
        pizza_map = {
            'cheese': CheesePizza,
            'veggie': VeggiePizza,
            'clam': ClamPizza,
            'pepperoni': PepperoniPizza
        }

        return pizza_map.get(pizza_type)()
