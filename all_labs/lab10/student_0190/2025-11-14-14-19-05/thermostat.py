class Thermostat:
    
    def __init__(self, temperature = 68):
        self.temperature = temperature
        self.schedule = {}

    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__(self):
        schedule_str = f"Default temperature: {self.temperature} degrees"
        for time, temp in sorted(self.schedule.items()):
            schedule_str += f"\n{time} {temp} degrees"
        return schedule_str
    
    def get_target_temperature(self, time):
        
        if not self.schedule:
            return self.temperature
        
        times = sorted(self.schedule.keys())

        if time < times[0]:
            return self.temperature
        
        target = times[0]
        for t in times:
            if t <= time:
                target = t
            else:
                break
        
        return self.schedule[target]

