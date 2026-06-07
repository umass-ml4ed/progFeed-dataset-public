# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__ (self, temp = 68):
        self.default_temp = temp
        self.schedules = {}
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    def __str__(self):
        lst = sorted(self.schedules)
        self.string = f"Default temperature: {self.default_temp} degrees"
        count = 0
        while count < len(lst):
                self.string += f"\n{lst[count]} {self.schedules[lst[count]]} degrees"
                count += 1
        return self.string
    def get_target_temperature(self, time):
         lst = sorted(self.schedules)
         if time < lst[0]:
              return self.default_temp
         elif time > lst[-1]:
              return self.schedules[lst[-1]]
         else:
            count = 0
            while count < (len(lst)):
                if time == lst[count]:
                    return self.schedules[lst[count]]
                elif count == len(lst):
                    if time > lst[count] and time < lst[-1]:
                        return self.schedules[lst[count]]
                elif time > lst[count] and time < lst[count+1]:
                    return self.schedules[lst[count]]
                count += 1
         

#dev = Thermostat(75)
#dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)

#print(dev.schedules)
#str(dev)
#print(dev.string)

#print(dev.get_target_temperature('23:00'))
#print(dev.get_target_temperature('16:35'))
#print(dev.get_target_temperature('05:55'))
#print(dev.get_target_temperature('08:00'))
#print(dev.get_target_temperature('12:00'))
#print(dev.get_target_temperature('22:30'))

