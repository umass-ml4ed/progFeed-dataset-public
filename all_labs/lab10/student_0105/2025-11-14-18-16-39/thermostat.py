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
        if str ==lst[0]:
            return self.schedule[lst[0]]
        for i in range(1, len(lst)-1):
            if str>=lst[i] and str < lst[i+1]:
                return self.schedule[lst[i]]
            elif str>lst[len(lst)-1]:
                return self.schedule[lst[len(lst)-1]] 
            else:
                return self.temp
        if len(lst) == 0:
            return self.temp          


dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev.get_target_temperature('23:00')) 
print(dev.get_target_temperature('16:35')) 
print(dev.get_target_temperature('05:55')) 


print(dev.get_target_temperature('08:00')) 

print(dev.get_target_temperature('12:00'))
 



