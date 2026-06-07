# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default_temp=68):
        self.default_temp =float(default_temp)
        self.schedules={}

    def add_schedule(self,time,temp):
        self.schedules[time]=float(temp)
    
    def __str__(self):
        return f"Default temperature: {int(self.default_temp)} degrees"
    
        if len(self.schedules) == 0:
            return result
        
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        
        return result

    
    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        
        times = sorted(self.schedules)

        if query_time < times[0]:
            return self.default_temp
        
        the_latest_time = None
        for t in times:
            if t <= query_time:
                the_latest_time = t
            else:
                break

        if the_latest_time is None:
            return self.default_temp

        return self.schedules[the_latest_time]
    
dev = Thermostat(75)
print(dev.get_target_temperature('23:00')) # 68.2
print(dev.get_target_temperature('16:35')) # 58.2
print(dev.get_target_temperature('05:55')) # 75
print(dev.get_target_temperature('08:00')) # 60.4
print(dev.get_target_temperature('12:00')) # 58.2




