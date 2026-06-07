# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,deftemp=68):
        self.deftemp = deftemp
        self.schedule={}
    def add_schedule(self,time,temp):
        self.schedule[time]=temp
    def __str__(self):
        final = f"Default temperature: {self.deftemp} degrees"
        if len(self.schedule) == 0:
            return final
        for i in sorted(self.schedule):
            final+=f"\n{i} {self.schedule[i]} degrees"
        return final
    def get_target_temperature(self, querytime):
        if len(self.schedule) == 0:
            return self.deftemp
        sortedschedule=sorted(self.schedule)
        if querytime<sortedschedule[0]:
            return self.deftemp
        latest=sortedschedule[0]
        for i in sortedschedule:
            if i<=querytime:
                latest=i
            else:
                break
        return self.schedule[latest]

    
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev)