# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self,default_temp=68):
        self.default_temp=default_temp
        self.schedule={}

    
    def add_schedule(self,time,temperature):
        self.schedule[time]=temperature

    def __str__(self):
        schedule=sorted(self.schedule)
        lst=[f"Default temperature: {self.default_temp} degrees"]
        for time in schedule:
            lst.append(f"{time} {self.schedule[time]} degrees")
        string="\n".join(lst)
        return string
    
    def get_target_temperature(self, time):
        schedule=sorted(self.schedule)

        if time<schedule[0]:
            return self.default_temp
        
        for t in schedule[::-1]:
            if t<=time:
                return self.schedule[t]

# dev = Thermostat(75)
# dev.add_schedule('08:00', 60.4)
# dev.add_schedule('19:35', 75.5)
# dev.add_schedule('09:30', 58.2)
# dev.add_schedule('22:39', 68.2)
# print(dev)

# print(dev.get_target_temperature('23:00'))
# print(dev.get_target_temperature('16:35'))
# print(dev.get_target_temperature('05:55'))
# print(dev.get_target_temperature('08:00'))
# print(dev.get_target_temperature('12:00'))
