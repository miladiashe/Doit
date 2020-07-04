class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -=val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if (self.value > 100):
            self.value = 100
