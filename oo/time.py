class Time:
    time = 0

    def __init__(self, time):
        self.time = time

    def second_to_minutes(self):
        return f'{self.time // 60} min {self.time % 60} sec'

    def seconds_to_hours(self):
        a = f'{self.time // 3600} hrs '
        return a + f'{self.time // 60} min {self.time % 60} sec'

    def seconds_to_days(self):
        a = f'{self.time // 86400} days '
        return a + f'{self.time // 3600} hrs '+f'{self.time // 60} min {self.time % 60} sec'

t=Time(9078)
print(t.seconds_to_days())
print(t.seconds_to_hours())
print(t.second_to_minutes())
