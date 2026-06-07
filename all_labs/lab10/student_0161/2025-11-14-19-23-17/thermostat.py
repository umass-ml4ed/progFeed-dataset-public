# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


class Thermostat:
    def __init__(self, num=68):
        self.schedule = {}
        self.temperature = num
    

    def add_schedule(self, time, temperature):

        self.schedule[time] = temperature
        sorted_keys = sorted(self.schedule.keys())
        sorted_schedule = {k: self.schedule[k] for k in sorted_keys}
        self.schedule = sorted_schedule

       #print(self.schedule)
    
    def __str__(self):
        to_prnt = []
        to_prnt.append(f"Default temperature: {self.temperature} degrees")
        for i in self.schedule:
            to_prnt.append(f"\n{i} {self.schedule[i]} degrees")
        return "".join(to_prnt)
    
    def get_target_temperature(self, time):
        final_time=""
        for i in self.schedule:
            sched_time = i.replace(":", ".")
            time = time.replace(":", ".")

            if sched_time > time:
                if not final_time:
                    return self.temperature
                break
            final_time = i

        return self.schedule[final_time] 



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
