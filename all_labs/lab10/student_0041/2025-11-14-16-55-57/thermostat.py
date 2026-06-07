# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature=68):
        self.temperature = temperature
        self.schedule = {} # dictionary to store schedule

        #Thermostat(75)

    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature # dictionaries automatically handle double cases

    def __str__(self):
        result = "Default temperature: " + str(self.temperature) + " degrees"

        for i in sorted(self.schedule):
            temperature = self.schedule[i] # i is the time
            result += "\n" + str(i) + " " + str(temperature) + " degrees"

        return result

    def get_target_temperature(self, qtime):
        latest = self.temperature # initialized with the default value

        for i in sorted(self.schedule):
            if(i <= qtime):
                latest = self.schedule[i] # since it is a dictionary

        return latest # will automatically return default if nothing is found bc of initilization
            
dev = Thermostat(75)

dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(Thermostat())
print(dev)

dev.get_target_temperature('23:00') # returns 68.2
dev.get_target_temperature('16:35') # returns 58.2
dev.get_target_temperature('05:55') # returns 75
dev.get_target_temperature('08:00') # returns 60.4
dev.get_target_temperature('12:00') # returns 58.2