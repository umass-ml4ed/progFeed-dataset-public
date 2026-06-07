# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

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
        lis = list(self.schedules.keys())
        for time in lis:
            float_time = time.replace(':', '.')
            lis[lis.index(time)] = float_time
        query_time = float(query_time.replace(':', '.'))
        a = len(lis)
        for i in range(a):
            if float(lis[i]) <= query_time <= float(lis[i+1]) or query_time > float(lis[-1]):
                time = str(lis[i].replace('.', ':'))
                return self.schedules[time]
        
dev = Thermostat()



dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)
        
        
        










