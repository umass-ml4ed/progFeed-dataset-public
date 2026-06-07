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
        times = sorted(self.schedules.keys(), key=hours_to_minutes)
        q = hours_to_minutes(query_time)


        if q < hours_to_minutes(times[0]):
            return self.temp


        for i in range(len(times) - 1):
            t1 = hours_to_minutes(times[i])
            t2 = hours_to_minutes(times[i+1])
            if t1 <= q < t2:
                return self.schedules[times[i]]

  
        return self.schedules[times[-1]]
















