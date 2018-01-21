
"""
Decorator pattern
"""


class Beverage(object):

    TALL = 0
    GRANDE = 1
    VENTI = 2

    def __init__(self, *args, **kwargs):
        self.description = ''
        self.size = self.GRANDE

    def cost(self):
        raise NotImplementedError

    def get_description(self):
        return self.description

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size


class HouseBlend(Beverage):

    PRICE_MAP = {
        Beverage.TALL: 1.0,
        Beverage.GRANDE: 2.0,
        Beverage.VENTI: 3.0
    }

    def __init__(self, *args, **kwargs):
        super(HouseBlend, self).__init__(*args, **kwargs)
        self.description = 'House Blend Coffee'

    def cost(self):
        return self.PRICE_MAP.get(self.get_size())


class Espresso(Beverage):

    PRICE_MAP = {
        Beverage.TALL: 2.0,
        Beverage.GRANDE: 3.0,
        Beverage.VENTI: 4.0
    }

    def __init__(self, *args, **kwargs):
        super(Espresso, self).__init__(*args, **kwargs)
        self.description = 'Espresso coffee'

    def cost(self):
        return self.PRICE_MAP.get(self.get_size())


class CondimentDecorator(Beverage):
    """
    Decorator abstract class
    """

    def __init__(self, *args, **kwargs):
        super(CondimentDecorator, self).__init__(*args, **kwargs)

    def get_description(self):
        raise NotImplementedError

    def cost(self):
        raise NotImplementedError


class Mocha(CondimentDecorator):

    PRICE_MAP = {
        Beverage.TALL: 0.5,
        Beverage.GRANDE: 0.6,
        Beverage.VENTI: 0.7
    }

    def __init__(self, beverage, *args, **kwargs):
        super(Mocha, self).__init__(*args, **kwargs)
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ' plus Mocha'

    def cost(self):
        return self.beverage.cost() + self.PRICE_MAP.get(self.get_size())


class Whip(CondimentDecorator):

    PRICE_MAP = {
        Beverage.TALL: 0.6,
        Beverage.GRANDE: 0.7,
        Beverage.VENTI: 0.8
    }

    def __init__(self, beverage, *args, **kwargs):
        super(Whip, self).__init__(*args, **kwargs)
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ' plus Whip'

    def cost(self):
        return self.beverage.cost() + self.PRICE_MAP.get(self.get_size())


class Soy(CondimentDecorator):

    PRICE_MAP = {
        Beverage.TALL: 0.7,
        Beverage.GRANDE: 0.8,
        Beverage.VENTI: 0.9
    }

    def __init__(self, beverage, *args, **kwargs):
        super(Soy, self).__init__(*args, **kwargs)
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ' plus Soy'

    def cost(self):
        return self.beverage.cost() + self.PRICE_MAP.get(self.get_size())


if __name__ == '__main__':
    espresso = Espresso()
    espresso.set_size(Beverage.VENTI)
    print espresso.get_description(), espresso.cost()

    espresso = Mocha(espresso)
    print espresso.get_description(), espresso.cost()

    espresso = Whip(espresso)
    print espresso.get_description(), espresso.cost()

    espresso = Soy(espresso)
    print espresso.get_description(), espresso.cost()
