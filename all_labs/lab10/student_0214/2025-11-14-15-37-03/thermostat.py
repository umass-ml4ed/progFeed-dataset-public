# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
class Thermostat:
    def __init__(self, temp = 68):
        self.temperature = temp
        self.schedule = {}
    def add_schedule(self, time, temp):
        self.schedule[time] = temp
    def __str__(self):
        lst = sorted(self.schedule)
        string_end = ""
        for key in lst:
            string_end += f"{key} {self.schedule[key]} degrees\n"
        string_start = f"Default Temperature: {self.temperature} degrees\n"
        string = string_start + string_end
        return string[:-1]
    def get_target_temperature(self, time):
        lst = sorted(self.schedule)
        if time not in lst:
            lst.append(time)
            new_lst = sorted(lst)
            pos = new_lst.index(time)
            if pos == 0:
                return self.temperature
            else:
                return self.schedule[new_lst[pos - 1]]
        else:
            return self.schedule[time]
                   

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)
print(dev.get_target_temperature('23:00')) 
print(dev.get_target_temperature('16:35')) 
print(dev.get_target_temperature('05:55')) 
print(dev.get_target_temperature('08:00')) 
print(dev.get_target_temperature('12:00')) 
