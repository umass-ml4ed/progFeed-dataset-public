# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        """
        Constructor for Thermostat class.
        
        Args:
            default_temp (float): Default temperature in Fahrenheit. Defaults to 68.
        """
        self.default_temp = default_temp
        self.schedules = {}  # Empty dictionary to store time-temperature pairs
    
    def add_schedule(self, time, temperature):
        """
        Add a time-temperature schedule to the thermostat.
        
        Args:
            time (str): Time in 'HH:MM' format
            temperature (float): Temperature in Fahrenheit
        """
        self.schedules[time] = temperature
    
    def __str__(self):
        """
        Return a string representation of the thermostat.
        
        Returns:
            str: Formatted string showing default temperature and all schedules
        """
        # Start with the default temperature line
        result = f"Default temperature: {self.default_temp} degrees"
        
        # If there are schedules, add them sorted by time
        if self.schedules:
            # Sort the times in ascending order
            sorted_times = sorted(self.schedules.keys())
            
            # Add each schedule on a new line
            for time in sorted_times:
                temp = self.schedules[time]
                result += f"\n{time} {temp} degrees"
        
        return result
    
    def get_target_temperature(self, query_time):
        """
        Get the target temperature for a given query time.
        
        Args:
            query_time (str): Query time in 'HH:MM' format
            
        Returns:
            float: Target temperature for the given time
        """
        # If no schedules exist, return default temperature
        if not self.schedules:
            return self.default_temp
        
        # Get all schedule times and sort them
        sorted_times = sorted(self.schedules.keys())
        
        # Find the latest time that is <= query_time
        candidate_time = None
        for time in sorted_times:
            if time <= query_time:
                candidate_time = time
            else:
                # We've passed the query time, so break
                break
        
        # If we found a candidate time, return its temperature
        if candidate_time is not None:
            return self.schedules[candidate_time]
        else:
            # If no candidate found (query_time is before all schedules), return default
            return self.default_temp