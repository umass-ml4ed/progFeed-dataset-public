# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68, sched = {}):
        self.temp = temp
        self.sched = sched
    def add_schedule(self, time:str, temp:float):
        self.sched[time] = temp
    def __str__(self):
        fstr = f'Default temperature: {self.temp} degrees'
        for time in self.sched:
            fstr += f'\n{time} {self.sched[time]} degrees'
        return fstr
    def get_target_temperature(self, query_time:str):
        sorted_list = sorted(self.sched.items())
        sorted_sched = dict(sorted_list)
        
        lower_bound = None
        upper_bound = None
        for i in range(len(sorted_list)):
            if sorted_list[i][0] <= query_time:
                lower_bound = sorted_list[i][0]
            else:
                upper_bound = sorted_list[i][0]
                break

        if lower_bound is None:
            return self.temp
        elif upper_bound is None:
            return sorted_list[-1][1]
        return sorted_sched[lower_bound]


dev = Thermostat(75)

dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev)

print(dev.get_target_temperature('23:00'))
print(dev.get_target_temperature('16:35'))
print(dev.get_target_temperature('05:55'))
print(dev.get_target_temperature('08:00'))
print(dev.get_target_temperature('12:00'))