# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default_temp=68):
        self.default_temp=default_temp
        self.schedules={}
    
    def add_schedule(self,time,temperature):
        self.schedules[time]=temperature

    def __str__(self):
        lines=[]
        lines.append(f"Default temperature: {self.default_temp} degrees")
        for time in sorted(self.schedules):
            temp=self.schedules[time]
            lines.append(f"{time} {temp} degrees")
        return "\n".join(lines)
    
    def get_target_temperature(self,query_time):
        if not self.schedules:
            return self.default_temp

        latest_time=None

        for time in self.schedules:
            if time<=query_time:
                if latest_time is None or time>latest_time:
                    latest_time=time
        if latest_time is None:
            return self.default_temp
        return self.schedules[latest_time]
    
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)
dev.get_target_temperature('23:00') 
dev.get_target_temperature('16:35') 
dev.get_target_temperature('05:55') 
dev.get_target_temperature('08:00') 
dev.get_target_temperature('12:00')
