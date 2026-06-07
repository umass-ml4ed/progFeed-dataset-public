# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        """Constructor: initializes default temperature and empty schedule dictionary."""
        self.default_temp = default_temp
        self.times = {} 

    def add_schedule(self, time, temperature):
        """Add or update a scheduled time → temperature pair."""
        self.times[time] = temperature

    def __str__(self):
        """Return formatted string containing default temp and sorted schedule entries."""
        result = f"Default temperature: {self.default_temp} degrees"
        if len(self.times) == 0:
            return result
        
        for time in sorted(self.times):
            temp = self.times[time]
            result += f"\n{time} {temp} degrees"

        return result

    def get_target_temperature(self, q_time):
        """Return the temperature that applies at the given query time."""
        times = sorted(self.times)

        if len(self.times) == 0:
            return self.default_temp
        #for when there is nothing sched'd

        latest = None 

        for t in times:
            if t <= q_time:
                latest = t
            else:
                break

        if latest is None:
            return self.default_temp
    
        return self.times[latest]