#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

class Thermostat:
    data = {}
    def __init__(self,temp=68):
        self.temp = temp
        self.schedule = {}
    def add_schedule(self,time,temp):
        self.schedule[time] = temp
    def __str__(self):
        ordered_times = sorted(self.schedule)
        output = f'Default temperature: {self.temp} degrees'
        if ordered_times:
            schedule_lines = [f'{time} {self.schedule[time]}' for time in ordered_times]
            output += '\n' + '\n'.join(schedule_lines)
        return output
    def get_target_temperature(self,target):
        ordered_times = sorted(self.schedule)
        smaller_times = []
    
        for time in ordered_times:
            time_hour, time_min = time.split(':')
            target_hour, target_min = target.split(':')
            if int(time_hour) < int(target_hour):
                smaller_times.append(time)
            elif int(time_hour) == int(target_hour):
                if int(time_min) <= int(target_min):
                    smaller_times.append(time)
        if not smaller_times:
            return self.temp
        else:
            return self.schedule[max(smaller_times)]


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
