#!/usr/bin/env python3

import math

class Modifier:
    def __init__(self, value=None, modifier=None):
        self.value = None
        self.modifier = None

        if value is None and modifier is None:
            value = 10

        if value is None and modifier is not None:
            self.modifier = modifier
            self.value = (modifier*2)+10
        else:
            self.value = value
            self.modifier = math.floor((value-10)/2)

    def modify(self, value=10):
        return value + self.modifier

    def increment(self, value=2):
        self.modifier += (value/2)
        self.value += value

    def decrement(self, value=2):
        self.modifier -= (value/2)
        self.value -= value

    def copy(self):
        return Modifier(value=self.value)

    def __repr__(self):
        if self.modifier < 0:
            return f'-{abs(self.modifier)} ({self.value})'

        return f'+{self.modifier} ({self.value})'
