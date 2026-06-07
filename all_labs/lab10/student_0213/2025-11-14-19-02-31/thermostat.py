# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:

    def __init__(self, temp=68):
        self.new_dict = {}
        self.new_dict[''] = temp

    def add_schedule(self, time, temp):
        self.dicty = {}
        self.dicty[time] = temp

    #def __str__(self):
        #lst = []
        #my_thermostat = sorted(self.dicty)
        #for t in my_thermostat:
            #lst.append(f'{t} {self.dicty[t]} degrees')
        #my_str = '\n'.join(lst)
        #return f'Default temperature: {self.new_dict['']} degrees\n{my_str}'

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)