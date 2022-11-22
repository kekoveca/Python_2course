class GasStation:
    # Конструктор, принимающий один параметр - ёмкость резервуара колонки
    # Резервуар создаётся пустой
    def __init__(self, capacity):
        self.capacity = capacity
        self.avail = 0
    # Залить в резервуар колонки n литров топлива
    # Если столько не влезает в резервуар - не заливать ничего, выбросить exception
    def fill(self, n):
        if n > self.capacity - self.avail:
            raise Exception()
        self.avail += n

    # Заправиться, забрав при этом из резервура n литров топлива
    # Если столько нет в резервуаре - не забирать из резервуара ничего, выбросить exception
    def tank(self, n):
        if self.avail < n:
            raise Exception()
        self.avail -= n

    # Запросить остаток топлива в резервуаре
    def get_limit(self):
        return self.avail

s = GasStation(1000)
s.fill(300)
print(s.get_limit())
s.tank(100)
s.fill(300)
print(s.get_limit())
for i in range(5):
    s.tank(50)
print(s.get_limit())
s.fill(1000)
for i in range(50):
    s.tank(100)
print(s.get_limit())
