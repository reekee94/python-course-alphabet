import uuid
from constants import *
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import random
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
    def __init__(self, name, garages=None):
        self.name = str(name)
        self.garages = garages if garages is not None else []
        self.register_id = uuid.uuid4()

    def hit_hat(self):
        return sum(g.hit_hat() for g in self.garages)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(map(lambda garage: len(garage.cars), self.garages))

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def add_car(self, car, garage=None):
        garage = garage or max(self.garages, key=lambda x: x.freeplace)
        if garage.freeplace > 0:
            garage.add_car(car)
        else:
            print('No places free places in', garage)

    @staticmethod
    def compare_cesar(cesar_list: list):
        return max((cesar for cesar in cesar_list), key=lambda x: x.hit_hat() )





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
        return self.number



class Garage:
    def __init__(self, town, places: int, garage_cars:[Car],  owner=None):
        self.town = town
        self.places = places
        self.owner = uuid.uuid4()
        self.cars = garage_cars if garage_cars is not None else []
        self.freeplace = self.places - len(self.cars)

    def add_car(self, other):
        if other not in self.cars and len(self.cars) < self.places:
            self.cars.append(other)
        return self.cars

    def remove_car(self, other):
         return self.cars.remove(other)

    def hit_hat(self):
         return sum(c.price for c in self.cars)



cars = []
for car_counter in range(random.randint(10, 100)):
    car = Car(price=random.uniform(100.5, 999.5),
              type=random.choice(CARS_TYPES),
              producer=random.choice(CARS_PRODUCER),
              mileage=random.uniform(0, 1000000),
              )
    cars.append(car)

car1 = Car(price=random.uniform(100.5, 999.5),
           type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER),
           mileage=random.uniform(0, 1000000),
           )
car2 = Car(price=random.uniform(100.5, 999.5),
           type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER),
           mileage=random.uniform(0, 1000000),
           )

print ("CAR1: ", car1)
print ("CAR2: ", car2)

# CHECK UUID CHANGE
print ("\n------CHECK UUID CHANGE--------")
old_number = car1.number
car1.number = car1.change_number()
print("The number {} of car {} was changed on: {}".format(old_number, car1.producer, car1.number))

# CHECK COMPARE
print ("\n-----CHECK COMPARE-------")
if car1.price <= car2.price:
    print(
        "price {} car {} biggest then price {} car {}".format(car2.price, car2.producer, car1.price, car1.producer))
else:
    print(
        "price {} car {} biggest then price {} car {}".format(car1.price, car1.producer, car2.price, car2.producer))

if car1.price < car2.price:
    print(
        "car {} price {} cheaper then car {} price {}".format(car1.producer, car1.price, car2.producer, car2.price))
else:
    print("car {} cheaper then car {}".format(car2.producer, car1.producer))

if car1.price == car2.price:
    print(
        "price {} car {} is equal to price {} car {}".format(car1.price, car1.producer, car2.price, car2.producer))

if car1.price != car2.price:
    print("price car {} isn't equal to price car {}".format(car1.producer, car2.producer))


print ("\n-----CHECK GARAGE------")
CESAR_NAME = ["Oleg", "Vitaliya", "Marina", "Grisha", "Petr"]
cesars = []
for cesar_counter in range(random.randint(2, 3)):
    garageslist = []
    for garage_counter in range(random.randint(1, 3)):
        count_cars = random.randint(1, 4)
        random_place = random.randint(0, 10)

        get_car = []
        for i in random.sample(cars, count_cars):
            if i not in get_car:
                cars.remove(i)
                get_car.append(i)

            if count_cars > random_place:
                raise ValueError("Count cars more then count place. RUN PGOGRAM AGAIN")
            else:
                garage_real = Garage(town=random.choice(TOWNS),
                                places=random_place,
                                garage_cars=get_car)
            garageslist.append(garage_real)
            print (garage_real)




    cesar = Cesar(name=random.choice(CESAR_NAME), garages=garageslist)
    cesars.append(cesar)

print ("\n-----CHECK CESAR------")
for item in cesars:
    print(item, "\n")

print ("THE RICHEST CESAR IS: ",(Cesar.compare_cesar(cesars)).name)

print("\n----CHECK ADD CARS----------")
print("BEFORE ADD NEW CAR: ", garageslist[0])
print("PRICE ALL CARS IN GARAGE BEFORE ADD CAR: ", garageslist[0].hit_hat())

print("\nAFTER ADD NEW CAR: ", garageslist[0].add_car(car1))
print("PRICE ALL CARS IN GARAGE AFTER ADD CAR: ", garageslist[0].hit_hat())

print("\nBEFORE REMOVE NEW CAR: ", garageslist[0])
print("\nCAR FOR REMOVE: ", garageslist[0].cars[0])
print("\nAFTER REMOVE NEW CAR: ", garageslist[0].remove_car(garageslist[0].cars[0]))

print("\nADD CAR TO FREE GARAGE: ", cesars[0].add_car(car1))
print("\nADD CAR TO SELECTED GARAGE: ", cesars[0].add_car(car2, garageslist[0]))
