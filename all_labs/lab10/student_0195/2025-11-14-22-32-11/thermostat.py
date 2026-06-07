# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

# class Thermostat:
#     def __init__(self, dtemp = 68):
#         self.dtemp = dtemp
#         self.sched = {}
    
#     def add_sched(self, time, temp):
#         self.sched[time] = temp

#     def __str__(self):
#         newsched = sorted(self.sched)
#         text = f"Default temperature: {self.dtemp} degrees"
#         for t in newsched:
#             temp = self.sched[t]
#             text += f"\n{t} {temp} degrees"
#         return text
    
#     def get_target_temperature(self, query_time):
#         sorted_time = sorted(self.sched.keys())
#         target_temp = self.dtemp
#         for sched_time in sorted_time:
#             if sched_time <= query_time:
#                 target_temp = self.sched[sched_time]
#             else:
#                 break
#         return target_temp














class Thermostat:
    def __init__(self,dtemp=68):
        #how to do values for temp with time
        self.dtemp=dtemp
        self.sched={}

    def add_sched(self, time:str, temp:float):
        #for i in self.dtemp:
        if time in self.sched:
            self.sched[time]=temp
        else:
            self.sched[time]=temp
        # return self.sched. ------------- I commented this
    
    def __str__(self):
        line=''
        #Default temperature: {dtemp} degrees\n
        newsched=sorted(self.sched)
        for i in newsched:
            temp=self.sched[i]
            line+=f'\n{i} {temp} degrees'#how to fix i
            
        return f'Default temperature: {self.dtemp} degrees{line}'
    
    def get_target_temperature(self, time:str):
        sorted_time=sorted(self.sched.keys())  
        target_temp = self.dtemp
        for sched_time in sorted_time:
            if sched_time <= time:
                target_temp = self.sched[sched_time]
            else:
                break
        return target_temp
        #x=0
        newsched.append(time)
        newsched=sorted(newsched)
        #for i in self.sched:
        if  time=='00:00' or (time==newsched[0] and (time not in self.sched)):
                #value=newsched[1]
            return self.dtemp
        elif time==newsched[0] and (time in self.sched):
            value=newsched[1]
            return self.sched[value]
        elif time=='23:59' or time==newsched[-1]:
            value=newsched[-2]
            return self.sched[value]
        else:
            for x in range(1,len(newsched)-1):
                if newsched[x]==time:
                    value=newsched[x-1]
                    return self.sched[value]