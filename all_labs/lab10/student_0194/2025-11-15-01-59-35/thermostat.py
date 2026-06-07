# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature=68):
        self.temperature = temperature
        self.schedule = {}
        
    def add_schedule(self, time, temp):
        self.schedule[time] = temp
    
    def __str__(self):
        str = f'Default temperature: {self.temperature} degrees\n'
        ordered = sorted(self.schedule)
        for i in ordered:
            str += f'{i} {self.schedule[i]} degrees\n'
        str = str.strip()
        return str
    
    def get_target_temperature(self, qTime):
        keys = list((self.schedule).keys())
        tTemp = self.temperature
        index = 0
        for t in range(len(keys)):
            # See if qTime is between last time and 23:59
            if (t == len(keys) - 1):
                if (int(qTime[0:2] + qTime[3:5]) >= int(keys[t][0:2] + keys[t][3:5]) and int(qTime[0:2] + qTime[3:5]) <= 2359):
                    tTemp = self.schedule[keys[t]]
                    return tTemp
            # See if qTime is equal to first time (this was bugging my code)
            if (keys[0] == qTime):
                tTemp = self.schedule[keys[t]]
                return tTemp
            # See if qTime is less than first time
            if (t == 0):
                if (int(qTime[0:2] + qTime[3:5]) >= 0 and int(qTime[0:2] + qTime[3:5]) < int(keys[t][0:2] + keys[t][3:5])):
                    return tTemp
            # Find which times qTime is between
            else:
                if (int(qTime[0:2] + qTime[3:5]) >= int(keys[t][0:2] + keys[t][3:5]) and int(qTime[0:2] + qTime[3:5]) < int(keys[index + 1][0:2] + keys[index + 1][3:5])):
                    tTemp = self.schedule[keys[t]]
                    return tTemp
            index += 1