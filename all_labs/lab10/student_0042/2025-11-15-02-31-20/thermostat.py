# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat():
    def __init__(self, temp=68):
        self.default = temp
        self.schedules = {}
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    def __str__(self):
        x = ""
        for item in sorted(self.schedules):
            x += f"\n{item} {self.schedules[item]} degrees"
        return str(f"Default temperature: {self.default} degrees" + x)
    def get_target_temperature(self, time):
        return interpretvalues(self.schedules, time, self.default)

def interpretvalues(schedulelist, given, default):
    #I put this in a separate function because it made it slightly easier to test
    #The autograder is marking it as wrong but I genuinely have no idea what is wrong with it,
    #It has worked for every test I put it through.
    z = schedulelist
    z["00:00"] = default
    z["23:59"] = default
    z = sorted(z)
    for item in z:
        if given < item:
            continue
        elif given >= item and given < z[z.index(item) + 1]:
            if item == "00:00":
                return default
            else:
                return schedulelist[item]
            
        




# dev = Thermostat(75)
# dev.add_schedule('08:00', 60.4)
# dev.add_schedule('19:35', 75.5)
# dev.add_schedule('09:30', 58.2)
# dev.add_schedule('22:39', 68.2)

# print(dev.get_target_temperature('23:00'))
# print(dev.get_target_temperature('16:35'))
# print(dev.get_target_temperature('05:55'))
# print(dev.get_target_temperature('08:00')) 
# print(dev.get_target_temperature('12:00'))



