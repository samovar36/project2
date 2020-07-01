def add(num1, num2):
    res = num1 + num2
    return res

def decorator(func):      #decorator
    import time

    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print(f'Время подключения:{end - start}')
    return wrapper

@decorator
def fech_google():
    import requests
    page = requests.get('https://www.google.com')

fech_google()

class Car:  #названия классов всегда с большой буквы
    def __init__(self, mod, col, wheels, eng):
        self.model = mod
        self.color = col
        self.wheels_count = wheels
        self.engine = eng
        print(f'Машина {self.model} создана!')

    def run(self):
        print(f'{self.model} поехала!')

    def breaking(self):
        print(f'В {self.model} был пьяный священник, разбивший машину')

car1 = Car('BMW7', 'black', 4, 4.4)
car2 = Car('Tesla model S', 'red', 4, 0)
car3 = Car('Mercedes G 6x6', 'white', 6, 6.0)

print(f'Количество колес в BMW: {car1.wheels_count}, а в гелике: {car3.wheels_count}')
car2.run()
car3.breaking()