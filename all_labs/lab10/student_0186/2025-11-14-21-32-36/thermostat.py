class Thermostat:
    def __init__(self,default_temp=68):
        self.default_temp=default_temp
        self.schedules={}
    def add_schedule(self,time,temperature):
        self.schedule[time]=temperature
    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        if len(self.schedules) == 0:
            return result
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            result += f"\n{time} {self.schedules[time]} degrees"
        return result
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        latest_temp = None
        for t in sorted(self.schedules):  
            if t <= query_time:
                latest_temp = self.schedules[t]
            else:
                break
        if latest_temp is None:
            return self.default_temp

        return latest_temp
