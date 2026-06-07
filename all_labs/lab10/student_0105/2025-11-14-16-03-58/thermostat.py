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
        line1 = f"Default Temperature: 68 degrees\n"
        for i in range(len(lst)-1):
            str = f"{lst[i]} {self.schedule[lst[i]]} degrees\n"
            other_lst.append(str)
        final_str = f"{lst[len(lst)]} {self.schedule[len(lst)]} degrees"
        return line1 + "".join(other_lst) + final_str
    def get_target_temperature(self, str):
        lst = sorted(self.schedule)
        for i in range(1, len(lst)):
            if str<lst[0]:
                return 68
            elif str>=lst[i] and str < lst[i+1]:
                return self.schedule[lst[i]]
            elif str>lst[len(lst)]:
                return self.schedule[lst[len(lst)]]           


dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
print(Thermostat())        
print(dev)
        

