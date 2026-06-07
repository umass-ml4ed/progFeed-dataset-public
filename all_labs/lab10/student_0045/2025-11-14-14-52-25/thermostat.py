# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}


    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            temperature = self.schedules[time]
            result += f"\n{time} {temperature} degrees"
        return result
    
    def get_target_temperature(query_time):
        if int(query_time[0])==0:    
            if int(query_time[1])<8:
                return 75
            if int(query_time[1])==8:
                return 60.4
            if int(query_time[1])==9:
                if int(query_time[3])<3:
                    return 60.4
                else:
                    return 58.2
        elif int(query_time[0])==1:
            if int(query_time[1])<9:
                return 58.2
            if int(query_time[1])==9:
                if int(query_time[3])<3:
                    return 58.2
                if int(query_time[3])==3:
                    if int(query_time[4])<5:
                        return 58.2
                    else:
                        return 75.5
        elif int(query_time[0])==2:
            if int(query_time[1])<2:
                return 75.5
            if int(query_time[1])==2:
                if int(query_time[3])<3:
                    return 75.5
                if int(query_time[3])==3:
                    if int(query_time[4])<9:
                        return 75.5
                    else:
                        return 68.2
            if int(query_time[1])>2:
                return 68.2
