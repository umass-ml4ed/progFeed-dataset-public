# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temperature=68):
        self.default_temperature = default_temperature
        self.schedules = {}
    
    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature
    
    def __str__(self):
        result = f"Default temperature: {self.default_temperature} degrees"
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            temperature = self.schedules[time]
            result += f"\n{time} {temperature} degrees"
        return result
    
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temperature
        
        latest_time = None
        for time in self.schedules:
            if time <= query_time:
                if latest_time is None or time > latest_time:
                    latest_time = time
        
        if latest_time is None:
            return self.default_temperature
        
        return self.schedules[latest_time]


if __name__ == "__main__":
    print("Test 1:")
    print(Thermostat())
    print()
    
    print("Test 2:")
    dev = Thermostat(75)
    dev.add_schedule('08:00', 60.4)
    dev.add_schedule('19:35', 75.5)
    dev.add_schedule('09:30', 58.2)
    dev.add_schedule('22:39', 68.2)
    print(dev)
    print()
    
    print("Test 3: Query times")
    print(f"dev.get_target_temperature('23:00') = {dev.get_target_temperature('23:00')}")
    print(f"dev.get_target_temperature('16:35') = {dev.get_target_temperature('16:35')}")
    print(f"dev.get_target_temperature('05:55') = {dev.get_target_temperature('05:55')}")
    print(f"dev.get_target_temperature('08:00') = {dev.get_target_temperature('08:00')}")
    print(f"dev.get_target_temperature('12:00') = {dev.get_target_temperature('12:00')}")