#! -*- coding: utf-8 -*-
"""
observer pattern and strategy patter
"""

from abc import ABCMeta


class Observer(object):

    __class__ = ABCMeta


class Subject(object):

    __class__ = ABCMeta

    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observer(self, *args, **kwargs):
        raise NotImplementedError


class Observer(object):
    """
    Interface of observer
    """
    __class__ = ABCMeta

    def update(self, *args, **kwargs):
        raise NotImplementedError


class DisplayBehavior(object):
    """
    abstract class of display behavior
    """

    __class__ = ABCMeta

    def display(self, *args, **kwargs):
        raise NotImplementedError


class DisplayCurrentCondition(DisplayBehavior):

    def display(self, *args, **kwargs):
        print 'display current condition'
        print args
        print kwargs


class DisplayStatistics(DisplayBehavior):

    def display(self, *args, **kwargs):
        print 'display statistics data'
        print args
        print kwargs


class DisplayElement(object):

    def __init__(self, *args, **kwargs):
        self.display_behavior = DisplayBehavior()

    def display(self, *args, **kwargs):
        self.display_behavior.display(*args, **kwargs)


class WeatherData(Subject):
    """
    Weather data which implements subject
    """

    def __init__(self, *args, **kwargs):
        self.__observers = []
        self.__temperature = None
        self.__humidity = None
        self.__pressure = None

    def register_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self, *args, **kwargs):
        for observer in self.__observers:
            observer.update(*args, **kwargs)

    def set_measurements(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

        self.measurement_changed()

    def measurement_changed(self):
        changed_weather_data = dict(
            temperature=self.__temperature,
            humidity=self.__humidity,
            pressure=self.__pressure
        )
        self.notify_observer(**changed_weather_data)


class CurrentConditionDisplay(Observer, DisplayElement):
    """
    当前天气显示板
    """

    def __init__(self, subject, *args, **kwargs):
        super(CurrentConditionDisplay, self).__init__(*args, **kwargs)
        self.__subject = subject
        self.__subject.register_observer(self)
        self.display_behavior = DisplayCurrentCondition()

    def update(self, *args, **kwargs):
        self.display(*args, **kwargs)


class StatisticsDisplay(Observer, DisplayElement):
    """

    """

    def __init__(self, subject, *args, **kwargs):
        super(StatisticsDisplay, self).__init__(*args, **kwargs)
        self.__subject = subject
        self.__subject.register_observer(self)
        self.display_behavior = DisplayStatistics()

    def update(self, *args, **kwargs):
        self.display(*args, **kwargs)


class HeatIndexDisplay(Observer, DisplayElement):
    """
    酷热指数显示板
    similar as CurrentConditionDisplay
    """

    def update(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    weather_data = WeatherData()
    current_condition_display = CurrentConditionDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    weather_data.set_measurements(10, 10, 10)
    weather_data.set_measurements(3, 3, 3)
