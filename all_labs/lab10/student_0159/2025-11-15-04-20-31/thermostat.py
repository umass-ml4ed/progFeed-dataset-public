# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


class Thermostat:
    def __init__(self, a=68):
        self.a = a     
        self.b = {}   

    def c(self, d, e):
        self.b[d] = e

    def __str__(self):
        s = f"Default temperature: {self.a} degrees"

        if len(self.b) == 0:
            return s

        for t in sorted(self.b):
            s += f"\n{t} {self.b[t]} degrees"

        return s

    def f(self, g):
        h = sorted(self.b)

        if len(h) == 0:
            return self.a

        last = None
        for t in h:
            if t <= g:
                last = t
            else:
                break

        if last is None:
            return self.a

        return self.b[last]