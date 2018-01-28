"""
factory patterns:

* abstract factory
"""


class NYClam(object):
    pass


class NYPepperoni(object):
    pass


class NYVeggie(object):
    pass


class NYCheese(object):
    pass


class ChicagoClam(object):
    pass


class ChicagoPepperoni(object):
    pass


class ChicagoVeggie(object):
    pass


class ChicagoCheese(object):
    pass


class PizzaIngredientFactory(object):

    def create_dough(self):
        pass

    def create_sauce(self):
        pass

    def create_cheese(self):
        pass

    def create_veggie(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_cheese(self):
        return NYCheese()

    def create_veggie(self):
        return NYVeggie()

    def create_pepperoni(self):
        return NYPepperoni()

    def create_clam(self):
        return NYClam()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_cheese(self):
        return ChicagoCheese()

    def create_veggie(self):
        return ChicagoVeggie()

    def create_pepperoni(self):
        return ChicagoPepperoni()

    def create_clam(self):
        return ChicagoClam()


class Pizza(object):

    def __init__(self, pizza_ingredient_factory):
        self.pizza_ingredient_factory = pizza_ingredient_factory

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass

    def __str__(self):
        return '%s with %s' % (self.__class__, self.pizza_ingredient_factory)


class CheesePizza(Pizza):

    def prepare(self):
        self.pizza_ingredient_factory.create_clam()


class VeggiePizza(Pizza):

    def prepare(self):
        self.pizza_ingredient_factory.create_veggie()


class PepperoniPizza(Pizza):

    def prepare(self):
        self.pizza_ingredient_factory.create_pepperoni()


class ClamPizza(Pizza):

    def prepare(self):
        self.pizza_ingredient_factory.create_clam()


class PizzaStore(object):

    def create_pizza(self, pizza_type):
        """
        let subclass to implement the abstract method, which is factory method
        """
        raise NotImplementedError

    def order_pizza(self, pizza_type):

        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type):
        pizza_map = {
            'cheese': CheesePizza,
            'veggie': VeggiePizza,
            'clam': ClamPizza,
            'pepperoni': PepperoniPizza
        }

        pizza_ingredient_factory = NYPizzaIngredientFactory()

        return pizza_map.get(pizza_type)(pizza_ingredient_factory)


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type):
        pizza_map = {
            'cheese': CheesePizza,
            'veggie': VeggiePizza,
            'clam': ClamPizza,
            'pepperoni': PepperoniPizza
        }

        pizza_ingredient_factory = ChicagoPizzaIngredientFactory()

        return pizza_map.get(pizza_type)(pizza_ingredient_factory)


if __name__ == '__main__':
    pizza_store = NYPizzaStore()
    pizza = pizza_store.order_pizza('cheese')
    print pizza

    pizza_store = ChicagoPizzaStore()
    pizza = pizza_store.order_pizza('veggie')
    print pizza
