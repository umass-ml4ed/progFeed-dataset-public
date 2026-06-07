# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default_temperature = 68):
        self.default = default_temperature
        self.schedule = {}


    def add_schedule(self, time, temperature):
        self.time = time
        self.temperature = temperature
        self.schedule['time'] = temperature
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)