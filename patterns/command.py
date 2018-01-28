
"""
Command patter
"""

from abc import ABCMeta


class Receiver(object):
    """
    receiver interface
    """
    pass


class Light(Receiver):

    def on(self):
        print 'Light is on'

    def off(self):
        print 'Light is off'


class GarageDoor(Receiver):

    def open(self):
        print '%s is open' % self.__class__

    def close(self):
        print '%s is close' % self.__class__


class Stereo(Receiver):

    def on(self):
        print '%s is on' % self.__class__

    def set_cd(self):
        print 'set cd'

    def set_volume(self, volume):
        print 'set volumen %s' % volume

    def off(self):
        print '%s is off' % self.__class__


class CeilingFan(Receiver):

    HIGH = 3
    MIDDLE = 2
    LOW = 1
    OFF = 0

    def __init__(self):
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH
        print 'speed is %s' % self.speed

    def middle(self):
        self.speed = self.MIDDLE
        print 'speed is %s' % self.speed

    def low(self):
        self.speed = self.LOW
        print 'speed is %s' % self.speed

    def off(self):
        self.speed = self.OFF
        print 'speed is %s' % self.speed

    def get_speed(self):
        return self.speed


class Command(object):
    """
    command interface
    """

    __class__ = ABCMeta

    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class GarageDoorOpenCommand(Command):

    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.open()

    def undo(self):
        self.garage_door.close()


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self):
        self.stereo.off()


class CeilingFanHighCommand(Command):

    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.current_speed = None

    def execute(self):
        self.current_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        {
            CeilingFan.OFF: self.ceiling_fan.off,
            CeilingFan.LOW: self.ceiling_fan.low,
            CeilingFan.MIDDLE: self.ceiling_fan.middle,
            CeilingFan.HIGH: self.ceiling_fan.high
        }[self.current_speed]()


class NoCommand(Command):
    """
    no-command object
    """
    def __init__(self):
        self.receiver = None

    def execute(self):
        pass

    def undo(self):
        pass


class MicroCommand(Command):
    """
    micro command. let an command object execute multip commands
    """
    def __init__(self, command_objects):
        self.command_objects = command_objects

    def execute(self):
        for command_object in self.command_objects:
            command_object.execute()

    def undo(self):
        for command_object in self.command_objects:
            command_object.undo()


class Invoker(object):
    """
    invoker interface
    """

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def response(self):
        self.command.execute()

    def undo(self):
        self.command.undo()


class SimpleRemoteControl(Invoker):

    def __init__(self):
        super(SimpleRemoteControl, self).__init__()
        self.undo_command = NoCommand

    def response(self):
        self.command.execute()
        self.undo_command = self.command

    def undo(self):
        self.undo_command.undo()


if __name__ == '__main__':
    controller = SimpleRemoteControl()

    light = Light()
    light_on_command = LightOnCommand(light)
    controller.set_command(light_on_command)
    controller.response()

    garage_door = GarageDoor()
    garage_door_open_command = GarageDoorOpenCommand(garage_door)
    controller.set_command(garage_door_open_command)
    controller.response()
    controller.undo()

    stereo = Stereo()
    stereo_on_with_cd_command = StereoOnWithCDCommand(stereo)
    controller.set_command(stereo_on_with_cd_command)
    controller.response()

    ceiling_fan = CeilingFan()
    ceiling_fan_high_command = CeilingFanHighCommand(ceiling_fan)
    controller.set_command(ceiling_fan_high_command)
    controller.response()
    controller.undo()

    micro_command = MicroCommand([light_on_command,
                                  garage_door_open_command,
                                  stereo_on_with_cd_command,
                                  ceiling_fan_high_command])
    controller.set_command(micro_command)
    controller.response()
    controller.undo()
