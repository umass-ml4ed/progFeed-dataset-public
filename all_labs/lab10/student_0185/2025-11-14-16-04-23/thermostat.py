# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.schedule = {}
        self.temp = temp

    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__(self):
        sort = sorted(self.schedule)
        lst = [f"Default temperature: {self.temp} degrees"]
        for pair in sort:
            lst.append(f"{pair} {self.schedule[pair]} degrees")
        return "\n".join(lst)
    
    def get_target_temperature(self, query):
        sort = sorted(self.schedule)
        if len(self.schedule) == 0:
            return self.temp
        if query > sort[-1]:
            return self.schedule[sort[-1]]
        if query < sort[0]:
            return self.schedule[sort[0]]
        for i in range(len(sort)-1):
            if (query >= sort[i]) and (query < sort[i+1]):
                return self.schedule[sort[i]]

