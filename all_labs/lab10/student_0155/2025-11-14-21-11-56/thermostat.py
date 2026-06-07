# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, start_temp=68):
        self.temp = start_temp
        self.schedule = {}
    

    def add_schedule(self, time, temp):
        self.schedule[time] = temp
    

    def __str__(self):
        sorted_schedule = sorted(self.schedule)
        time_temps = []
        for i in sorted_schedule:
            string = f'{i} {self.schedule[i]} degrees'
            time_temps.append(string)
        final_timetemps = "\n".join(time_temps)

        return (f'Default temperature: {self.temp} degrees\n' + final_timetemps).strip('\n')
    
    def get_target_temperature(self, time):
        
        sorted_schedule = sorted(self.schedule)
        #print(sorted_schedule)

        time_hour_minute = time.split(":")
        time_hour = float(time_hour_minute[0])
        time_minute = float(time_hour_minute[1])

        #print((time_hour, time_minute))
        
        last_temp = self.temp
        for t in sorted_schedule:
            
            schedule_hour_minute = t.split(":")
            schedule_hour = float(schedule_hour_minute[0])
            schedule_minute = float(schedule_hour_minute[1])

            #print((schedule_hour, schedule_minute))
            if time_hour < schedule_hour or (time_hour == schedule_hour and time_minute < schedule_minute):
                return last_temp
            else:
                last_temp = self.schedule[t]
                continue
        return last_temp


#john = Thermostat(75)
#print(john)
#john.add_schedule('08:00', 76)
#john.add_schedule('07:00', 62)
#john.add_schedule('11:00', -1000)
#print(john)
#print(john.get_target_temperature('07:31'))
#print(john.get_target_temperature('08:32'))
#print(john.get_target_temperature('21:32'))