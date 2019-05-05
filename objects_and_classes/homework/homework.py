import uuid
from constants import *
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути. __str__ and __repr__

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі -  isinstance()
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


class Cesar:
    def __init__(self, name, garages=0, register_id):
        self.name = str(name)
        self.garages = garages if garages is not None else []
        self.register_id = register_id if register_id else uuid.uuid4()

    def hit_hat(self):
        return sum(g.hit_hat() for g in self.garages)

    def garages_count(self):
        return len(self.garages)
    def cars_count(self):
        return sum(len(c.cars) for c in self.garages)

    def __lt__(self, other):
        return hit_hat(self) < hit_hat(other)

    def __eq__(self, other):
        return hit_hat(self) == hit_hat(other)

    def __le__(self, other):
        return hit_hat(self) <= hit_hat(other)

    def add_car(self, car, garage=None):
        if garage == None:
            garage = max(self.garages, key=g.freeplaces for self.garages)
        elif garage.freeplace > 0:
            garage.add(car)
        else:
            print('No places free places in' garage)







class Car:
    def __init__(self, price, type, producer, mileage):
        self.price = float(price)
        self.type = type

        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = float(mileage)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, v):
        if v not in CARS_TYPES:
            raise Exception('Types must be one of: {0}.'.format(CARS_TYPES))
        self._type = v
    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, value):
        if value not in CARS_PRODUCER:
            raise Exception('Producer must be one of: {0}.'.format(CARS_PRODUCER))
        self._producer = value

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __str__(self):
        return "Car (price:{0}, car_type:{1}, producer:{2}, mileage:{3}, number:{4})".format(
            self.price, self.type, self.producer, self.mileage, self.number)
    def __repr__(self):
        return "Car (price:{0}, car_type:{1}, producer:{2}, mileage:{3}, number:{4})".format(
            self.price, self.type, self.producer, self.mileage, self.number)

    def change_number(self):
        self.number = uuid.uuid4()



class Garage:
    def __init__(self, town = TOWNS, places = 3, owner=None):
        self.town = town
        self.places = int(places)
        self.owner = uuid.uuid4()
        self.cars = []
        self.freeplace = self.places - len(self.cars)

    def __add__(self, other):
        if other not in self.cars and len(self.cars) < self.places:
            self.cars.append(other)
        return self.cars

     def __del__(self, other):
         return self.cars.remove(other)

     def hit_hat(self):
         return sum(c.price for c in self.cars)


