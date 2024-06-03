from typing import List
from datetime import datetime
class User:
    def __init__(self, username: str, email: str):
        self._username = username
        self._email = email
    def get_details(self):
        return f'Username: {self._username}, Email: {self._email}'
class Customer(User):
    def __init__(self, username: str, email: str, address: str):
        super().__init__(username, email)
        self._address = address
        self._orders: List[Order] = []
    def place_order(self, order):
        self._orders.append(order)
    def get_details(self):
        return f'Customer: {super().get_details()}, Address: {self._address}'
class DeliveryPerson(User):
    def __init__(self, username: str, email: str, vehicle: str):
        super().__init__(username, email)
        self._vehicle = vehicle
    def get_details(self):
        return f'Delivery Person: {super().get_details()}, Vehicle: {self._vehicle}'
class FoodItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
class Menu:
    def __init__(self):
        self.food_items: List[FoodItem] = []
    def add_food_item(self, food_item: FoodItem):
        self.food_items.append(food_item)
    def get_menu(self):
        return [f"{item.name}: ${item.price}" for item in self.food_items]
class Restaurant:
    def __init__(self, name: str):
        self.name = name
        self.menu = Menu()
    def add_food_item_to_menu(self, food_item: FoodItem):
        self.menu.add_food_item(food_item)
    def get_menu(self):
        return self.menu.get_menu()
class OrderItem:
    def __init__(self, food_item: FoodItem, quantity: int):
        self.food_item = food_item
        self.quantity = quantity
    def get_total_price(self):
        return self.food_item.price * self.quantity
class Order:
    def __init__(self, customer: Customer, restaurant: Restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.order_items: List[OrderItem] = []
        self.order_time = datetime.now()
    def add_order_item(self, order_item: OrderItem):
        self.order_items.append(order_item)
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.order_items)
class Delivery:
    def __init__(self, order: Order, delivery_person: DeliveryPerson, delivery_time: datetime):
        self.order = order
        self.delivery_person = delivery_person
        self.delivery_time = delivery_time
    def get_delivery_details(self):
        return f"Order by {self.order.customer.get_details()} delivered by {self.delivery_person.get_details()} at {self.delivery_time}"

if __name__ == "__main__":
    restaurant = Restaurant("Burger Club")
    pizza = FoodItem("Pizza", 12.0)
    burger = FoodItem("Burger", 9.0)
    french_fries = FoodItem("French Fries", 5.0)
    restaurant.add_food_item_to_menu(pizza)
    restaurant.add_food_item_to_menu(burger)
    restaurant.add_food_item_to_menu(french_fries)

    customer = Customer("daria_sotnikova", "d.sot1995@gmail.com", "st. Heroiv Dripra 12")

    order = Order(customer, restaurant)
    order.add_order_item(OrderItem(pizza, 2))
    order.add_order_item(OrderItem(burger, 1))
    order.add_order_item(OrderItem(french_fries, 3))

    customer.place_order(order)

    delivery_person = DeliveryPerson("alex_dom", "alex.domritskyi@gmail.com", "Bike")

    delivery = Delivery(order, delivery_person, datetime.now())

    print(customer.get_details())
    print(restaurant.get_menu())
    print(f"Total Order Price: ${order.get_total_price()}")
    print(delivery.get_delivery_details())