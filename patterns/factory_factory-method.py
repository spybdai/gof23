"""
factory patterns:
* factory method
"""


class Pizza(object):

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass

# More pizzas


class NYCheesePizza(Pizza):
    pass


class NYVeggiePizza(Pizza):
    pass


class NYClamPizza(Pizza):
    pass


class NYPepperoniPizza(Pizza):
    pass


class ChicagoCheesePizza(Pizza):
    pass


class ChicagoVeggiePizza(Pizza):
    pass


class ChicagoClamPizza(Pizza):
    pass


class ChicagoPepperoniPizza(Pizza):
    pass


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
            'cheese': NYCheesePizza,
            'veggie': NYVeggiePizza,
            'clam': NYClamPizza,
            'pepperoni': NYPepperoniPizza
        }

        return pizza_map.get(pizza_type)()


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type):
        pizza_map = {
            'cheese': ChicagoCheesePizza,
            'veggie': ChicagoVeggiePizza,
            'clam': ChicagoClamPizza,
            'pepperoni': ChicagoPepperoniPizza
        }

        return pizza_map.get(pizza_type)()


if __name__ == '__main__':
    pizza_store = NYPizzaStore()
    pizza = pizza_store.order_pizza('cheese')
    print pizza

    pizza_store = ChicagoPizzaStore()
    pizza = pizza_store.order_pizza('veggie')
    print pizza
