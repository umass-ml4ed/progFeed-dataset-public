# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self._temperature = temp

        default_temp=68
        schedule={}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature  

    def __str__():
        return f'Temperature: {self._temperature}°F'
    
    def get_target_temperature(time):



dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
