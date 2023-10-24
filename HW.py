class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, table) -> None:
        self.table = table
        self.dishes = []


#Реализация добавления блюда в заказ
    def add_dish(self, dish):
        self.dishes.append(dish)

# Реализцаия удаления блюда из заказа
    def remove_dish(self, dish):
        self.dishes.remove(dish)

#Реализация расчета общей стоимости заказов
    def calculate_total(self):
        total = 0
        for dish in self.dishes:
            total += dish.price
        return total
    
#Реализация вывода информации о заказе
def print_order(order):
    print("заказ на", order.table)
    for dish in order.dishes:
        print(f' - {dish.name}, {dish.price}')
    total = order.calculate_total()
    print(f'Общая стоимость: {total} руб.')


#создание блюд
dish1 = Dish("Котлета по киевски", 119.99)
dish2 = Dish("Пюре", 29.99 )
dish3 = Dish("Томатный суп", 49.99)

#Создание заказов
order1 = Order("Стол №1")
order2 = Order("Стол №2")

# Добавление блюд в заказы
order1.add_dish(dish1)
order1.add_dish(dish2)
order2.add_dish(dish3)

# Вывод информации о заказе
print_order(order1)
print_order(order2)
