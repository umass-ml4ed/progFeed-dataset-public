# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.curr_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, newtemp):
        self.schedules[f'{time}'] = f'{newtemp}'
    def __str__(self):
        string = str()
        string +=(f"Default temperature: {self.curr_temp} degrees")
        for time in (sorted(self.schedules)):
                string += (f"\n{time} {self.schedules[time]} degrees")
        return string
    def get_target_temperature(self, time):
        erm =sorted(self.schedules, reverse = True)
        count = 0
        for i in erm:
            count += 1
            if count == (len(self.schedules)) and (i <= time) != True:
                print(self.curr_temp)
            elif i <= time:
                print(self.schedules[i])
                break
            
            
             


dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
dev.get_target_temperature('23:00')
dev.get_target_temperature('16:35')
dev.get_target_temperature('05:55') 
dev.get_target_temperature('08:00') 
dev.get_target_temperature('12:00')
            
        
        

    