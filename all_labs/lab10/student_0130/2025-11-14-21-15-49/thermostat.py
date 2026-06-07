#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED


class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp      
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature
    
    def __str__(self):
    
        result = f"Default temperature: {self.default_temp} degrees"

        
        if not self.schedules:
            return result

    
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"

        return result

    def get_target_temperature(self, query_time):
       
    
        if not self.schedules:
            return self.default_temp

    
        sorted_times = sorted(self.schedules.keys())

        
        if query_time < sorted_times[0]:
            return self.default_temp

       
        for i in range(len(sorted_times) - 1):
            t1 = sorted_times[i]
            t2 = sorted_times[i + 1]

            
            if t1 <= query_time < t2:
                return self.schedules[t1]


        return self.schedules[sorted_times[-1]]

