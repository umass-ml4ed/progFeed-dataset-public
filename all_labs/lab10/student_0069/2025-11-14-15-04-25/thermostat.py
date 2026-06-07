# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


class Thermostat:

    def __init__(self,temp = 68 ):
        self.temp = temp 
        self.schedule = {}

dev = Thermostat(75)
print(dev.temp)
print(dev.schedule)

def add_schedule(self,time, temp):
    self.schedule[time] = temp

dev.add_schedule('08:00', 60.4)
print(dev.schedule)

def __str__(self):
    result = ("Default temperature: {self.temp} degrees")
    if not self.schedule:
        return result 
    result += "\n"
    for time in sorted(self.schedule):
        temp= self.schedule[time]
        result += f"{time} {temp} degrees\n"

    return result.rstrip("\n") 
print(Thermostat())
print(dev)

def get_target_temperature(self,query_time):
    if not self.schedule:
        return self.temp

   
    times = sorted(self.schedule)


    if query_time < times[0]:
        return self.temp

    
    latest_time = times[0]   

    for t in times:
        if t <= query_time:
            latest_time = t
        else:
            break

    
    return self.schedule[latest_time]
