# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from typing import Dict

class Thermostat:

    def __init__(self, default_temperature: float = 68) -> None:
        
        self.default_temperature: float = float(default_temperature)
        self.schedules: Dict[str, float] = {}

    def add_schedule(self, time: str, temperature: float) -> None:
        self.schedules[time] = float(temperature)

    def __str__(self) -> str:
        lines = [f"Default temperature: {self.default_temperature} degrees"]
        for t in sorted(self.schedules):
            lines.append(f"{t} {self.schedules[t]} degrees")
        return "\n".join(lines)

    def get_target_temperature(self, query_time: str) -> float:

        if not self.schedules:
            return self.default_temperature

        times = sorted(self.schedules)
        if query_time < times[0]:
            return self.default_temperature

        latest_time = times[0]
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break
        return self.schedules[latest_time]
