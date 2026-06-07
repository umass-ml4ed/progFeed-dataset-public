# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat():
    def __init__ (self, default_temp = 68):
        self.def_temp = default_temp
        self.schedule = {}
    
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__ (self, default_temp, time, temperature):
        return f"Default temperature: {default_temp} degrees \n {time} {temperature} "

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)