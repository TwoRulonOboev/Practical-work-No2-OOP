class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def minutes_until_midnight(self):
        total_minutes = 24 * 60
        current_minutes = self.hours * 60 + self.minutes
        return total_minutes - current_minutes

    def add_minutes(self, extra_minutes=100):
        total_minutes = self.hours * 60 + self.minutes + extra_minutes
        self.hours = (total_minutes // 60) % 24
        self.minutes = total_minutes % 60

    def __str__(self):
        return f"Текущее время: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    