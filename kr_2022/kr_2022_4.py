class Clock:
    # Служебные методы, если нужны
    def __init__(self):
        self.hour = 0
        self.minute = 0

    # Передвинуть время вперёд на minutes минут. Если minutes отрицательное - выбросить exception.
    def tick(self, minutes):
        if minutes < 0:
            raise(Exception)
        else:
            hours = minutes // 60
            self.hour += hours 
            minutes_ost = minutes % 60
            if minutes_ost + self.minute >= 60:
                self.hour = self.hour + 1
                self.minute = minutes_ost + self.minute - 60
            else:
                self.minute += minutes_ost
            if self.hour > 23:
                self.hour = self.hour % 24


    # Вернуть текущее время как tuple из часов и минут.
    def get_time(self):
        return (self.hour, self.minute)


c = Clock()
print(c.get_time())
c.tick(60 * 24 + 30)
print(c.get_time())