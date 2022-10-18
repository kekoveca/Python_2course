class Car:
    def __init__(self, capacity, speed, number):
        self.capacity = capacity
        self.speed = speed
        self.number = number

    def __repr__(self):
        return f"<Car capacity:{self.capacity} speed:{self.speed} number:{self.number}>"

    def __eq__(self, other):
        if type(other) != type(self): 
            return False
        return self.number == other.number

    def __hash__(self):
        self.tmp = [ord(el) for el in list(self.number)]
        self.tmp = ''.join(str(e) for e in self.tmp)
        return int(self.tmp)

# Создадим несколько машин
# Причём a и c - одна и та же машина с точки зрения сравнения
a = Car(100, 100, "asd")
b = Car(100, 100, "zzz")
c = Car(200, 50, "asd")

# Эти не равны
print(a == b)
# Эти равны
print(a == c)

# А эта пара примеров должна не упасть
# и корректно сказать, что машина не равна ни None, ни целому числу
print(a == None)
print(a == 1)

# Попробуем сложить машины в set
s = set()
s.add(a)
s.add(b)
s.add(c)
s.add(a)
s.add(a)

# Ожидаем увидеть номера двух машин,
# так как всё остальное в описанной логике является дублями
print("=== Cars in set ===")
for z in sorted(s, key=lambda e: e.number):
    print(z.number)