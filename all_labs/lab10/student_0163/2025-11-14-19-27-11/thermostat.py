# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp=default_temp
        self.schedules={}

    def add_schedule(self, time, temperature):
        self.schedules[time]=temperature
    
    def __str__(self):
        sorted_keys=sorted(self.schedules)
        bingle=f"Default temperature: {self.default_temp} degrees"
        for i in sorted_keys:
            bingle+= f"\n{i} {self.schedules[i]} degrees"
        return bingle
    
    def get_target_temperature(self,time):
        lis=[]
        for i in self.schedules:
            hour_check=int(i[0:2])
            hour_target=int(time[0:2])
            min_check=int(i[3:])
            min_target=time(i[3:])
            if (hour_check<=hour_target) or (min_check<=min_target):
                lis.append(i)
        if not lis:
            return self.default_temp
        else:
            return max(lis)