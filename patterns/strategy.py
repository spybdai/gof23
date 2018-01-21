from abc import ABCMeta


class FlyBehavior(object):
    __class__ = ABCMeta

    def fly(self):
        raise NotImplementedError


class QuackBehavior(object):
    __class__ = ABCMeta

    def quack(self):
        raise NotImplementedError


class Duck(object):

    def __init__(self, *args, **kwargs):
        self.fly_behavior = FlyBehavior()
        self.quack_behavior = QuackBehavior()

    def swim(self):
        pass

    def display(self):
        pass

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior


class FlyWithWings(FlyBehavior):

    def fly(self):
        print 'Fly with wings'


class FlyNoWay(FlyBehavior):

    def fly(self):
        print 'I cannot fly'


class FlyRocketPowered(FlyBehavior):

    def fly(self):
        print 'Fly with rocket power'


class Quack(QuackBehavior):

    def quack(self):
        print 'Quack'


class MuteQuack(QuackBehavior):

    def quack(self):
        print 'I cannot quack'


class Squeak(QuackBehavior):

    def quack(self):
        print 'Squeak'


class MallardDuck(Duck):

    def __init__(self, *args, **kwargs):
        super(MallardDuck, self).__init__(*args, **kwargs)
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()


class ModelDuck(Duck):

    def __init__(self, *args, **kwargs):
        super(ModelDuck, self).__init__(*args, **kwargs)
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()


if __name__ == '__main__':

    # duck = Duck()
    # duck.fly()

    mallard_duck = MallardDuck()
    mallard_duck.fly()
    mallard_duck.quack()

    model_duck = ModelDuck()
    model_duck.fly()
    model_duck.quack()

    model_duck.set_fly_behavior(FlyRocketPowered())
    model_duck.fly()
