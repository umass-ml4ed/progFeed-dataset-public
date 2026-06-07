# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
class Thermostat():
    def __init__(self,default_temp=68):
        self.default_temp=default_temp
        self.dictionary={}

    def add_schedule(self,time,temp):
        self.dictionary[time]=temp
    
    def __str__(self):
        result=f'Default temperature: {self.default_temp} degrees'
        for value in sorted(self.dictionary):
            result+=f'\n{value}:{self.dictionary[value]}'
        return result
    
    def get_target_temperature(self,time):
        sdict=sorted(self.dictionary)
        temp=self.default_temp
        for value in sdict:
            if value<=time:
                temp= self.dictionary[value]
        return temp
    

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)
print(dev.get_target_temperature('23:00'))
       
        
