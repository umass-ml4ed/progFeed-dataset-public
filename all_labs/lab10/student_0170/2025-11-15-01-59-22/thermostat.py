# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, def_temp = 68):
        self.def_temp = def_temp
        self.schedules = {}

    def add_schedule(self,time,temp):
        self.schedules[time] = temp
    
    def __str__(self):
        slist = [f"Default Temperature: {self.def_temp} degrees"]
        for time in sorted(self.schedules):
            temp = (self.schedules)[time]
            slist.append(f"{time} {temp} degrees")
        return "\n".join(slist)
    
    def get_target_temperature(self,time):
        latest_time = None
        for t in sorted(self.schedules):
            if t <= time:
                latest_time = t
            else:
                break
        if latest_time is None:
            return self.def_temp
        return self.schedules[latest_time]
    

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

##print(dev)