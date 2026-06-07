from typing import Dict

class Thermostat:
    def __init__(self, default_temperature: float = 68) -> None:
        self.default_temperature: float = float(default_temperature)
        self.schedules: Dict[str, float] = {}

    def add_schedule(self, time: str, temperature: float) -> None:
        self.schedules[time] = float(temperature)

    def __str__(self) -> str:
        def _fmt_default(temp: float) -> str:
            # For the default temperature only, avoid trailing .0 when it's an integer
            return str(int(temp)) if float(temp).is_integer() else str(temp)

        lines = [f"Default temperature: {_fmt_default(self.default_temperature)} degrees"]
        for t in sorted(self.schedules):
            # Keep schedule temps using normal float -> str behavior (e.g., 69.0)
            lines.append(f"{t} {str(self.schedules[t])} degrees")
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
