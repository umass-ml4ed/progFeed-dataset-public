# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp=68.0):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        default_temp_str = str(self.default_temp)
        if default_temp_str.endswith('.0'):
            default_temp_str = default_temp_str[:-2]
            
        result = f"Default temperature: {default_temp_str} degrees\n"
        
        sorted_times = sorted(self.schedules.keys())
        
        schedule_lines = []
        for time in sorted_times:
            temp = self.schedules[time]
            schedule_lines.append(f"{time} {temp} degrees")
            
        result += "\n".join(schedule_lines)
        
 
        if not schedule_lines:
            return result.rstrip('\n')
            
        return result
        
    def get_target_temperature(self, query_time):
        sorted_times = sorted(self.schedules.keys())
        
        if not sorted_times:
            return self.default_temp
        
        target_time = None
        for time in sorted_times:
            if time <= query_time:
                target_time = time
            else:
                break

        if target_time is not None:
            return self.schedules[target_time]
        
        return self.default_temp
