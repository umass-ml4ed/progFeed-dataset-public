# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, a=68):
        self.a = a     
        self.b = {}   

    def add_schedule(self, c, d):
        self.b[c] = d

    def __str__(self):
        s = f"Default temperature: {self.a} degrees"

        if len(self.b) == 0:
            return s

        for t in sorted(self.b):
            s += f"\n{t} {self.b[t]} degrees"

        return s

    def get_target_temperature(self, e):
        f = sorted(self.b)

        if len(f) == 0:
            return self.a

        last = None
        for t in f:
            if t <= e:
                last = t
            else:
                break

        if last is None:
            return self.a

        return self.b[last]
