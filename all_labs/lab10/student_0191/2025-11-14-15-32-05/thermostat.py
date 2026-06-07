# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp = temp
        self.schedule = {}

    def add_schedule(self, time, temp):
        self.schedule[time] = temp

    def __str__(self):
        print_statements = [f"Default temperature: {self.temp} degrees"]
        sorted_times = sorted(self.schedule)
        for time in sorted_times:
            temp = self.schedule[time]
            print_statements.append(f"{time} {temp} degrees")

        return "\n".join(print_statements)
    
    # def get_target_temperature(self, temp):
    #     sorted_times = sorted(self.schedule)
    #     if temp < sorted_times[0]:
    #         return self.temp
    #     elif temp > sorted_times[-1]:
    #         return self.schedule[sorted_times[-1]]
        
    #     for i in range(len(sorted_times)):
    #         if sorted_times[i] > temp:
    #             return self.schedule[sorted_times[i-1]]
    #         elif sorted_times[i] == temp:
    #             return self.schedule[sorted_times[i]]

    def get_target_temperature(self, query_time):
        sorted_times = sorted(self.schedule)

        if not self.schedule:
            return self.temp

        if query_time < sorted_times[0]:
            return self.temp

        last_time = None
        for time in sorted_times:
            if time <= query_time:
                last_time = time
            else:
                break   

        if last_time:
            return self.schedule[last_time]
        else:
            return self.temp


dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev.get_target_temperature('23:00')) 
print(dev.get_target_temperature('16:35')) 
print(dev.get_target_temperature('05:55'))
print(dev.get_target_temperature('08:00'))
print(dev.get_target_temperature('12:00'))

