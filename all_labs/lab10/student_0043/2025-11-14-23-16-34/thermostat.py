# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def hours_to_minutes(time):
        h, m = map(int, time.split(':'))
        minutes = int(h)*60 + int(m) 
        return minutes


class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp 
        self.schedules = {}
    
    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        temp = self.temp
        lis = []
        lis.append(f'Default temperature: {temp} degrees')
        for i in sorted(self.schedules):
            time = str(i)
            temps = str(self.schedules[time])
            lis.append(f"\n{time} {temps} degrees")
        return ''.join(lis)
    
    
    def get_target_temperature(self, query_time):
        lis = sorted(list(self.schedules.keys()))
        for i in range(len(lis)-1):
            if hours_to_minutes(lis[i]) <= hours_to_minutes(query_time) <= hours_to_minutes(lis[i+1]):
                temp = self.schedules[lis[i]]
            if hours_to_minutes(query_time) < hours_to_minutes(lis[0]):
                temp = self.temp
            if hours_to_minutes(query_time) > hours_to_minutes(lis[-1]):
                temp = self.schedules[lis[-1]]
        return temp
















