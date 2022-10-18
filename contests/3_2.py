class MoneyBox:
    # Конструктор и деструктор, если нужны
    def __init__(self):
        self.box = []
    # Добавить монетку достоинством value
    def add_coin(self, value):
        self.box.append(int(value))
    # Получить текущее количество монеток в копилке
    def get_coins_number(self):
        return len(self.box)
    # Получить текущее общее достоинство всех монеток
    def get_coins_value(self):
        return sum(self.box)

m = MoneyBox()
# Добавили монетку достоинством 10
m.add_coin(10)
# Добавили монетку достоинством 5
m.add_coin(5)

# Ожидаем, что монеток внутри 2 штуки
print(m.get_coins_number())
# Ожидаем, что общее достоинство всех монеток 15
print(m.get_coins_value())