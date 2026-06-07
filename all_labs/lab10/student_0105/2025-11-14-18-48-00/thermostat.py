# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.schedule = {}
    def add_schedule(self, time, temp):
        self.schedule[time] = temp
    def __str__(self):
        lst = sorted(self.schedule)
        other_lst = []
        for i in range(len(lst)):
            str = f"\n{lst[i]} {self.schedule[lst[i]]} degrees"
            other_lst.append(str)
        return f"Default temperature: {self.temp} degrees" + "".join(other_lst)
    def get_target_temperature(self, str):
        lst = sorted(self.schedule)
        for i in range(len(lst)-1):
            if str >= lst[i] and str < lst[i+1]:
                return self.schedule[lst[i]]
            elif str < lst[0]:
                return self.temp
            elif str > lst[len(lst)-1]:
                return self.schedule[lst[len(lst)-1]]
            if len(lst) == 0:
                return self.temp


dev = Thermostat()

print(dev.get_target_temperature('23:16'))




