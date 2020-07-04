class calculator:
    def __init__(self, by):
        self.numbers = by

    def sum(self):
        sss = 0
        for n in self.numbers:
            sss+=n
        return sss
    def avg(self):
        ssss = self.sum()
        ssss = ssss/len(self.numbers)
        return ssss
