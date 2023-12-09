# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Train:
    def __init__(self, number_of_places: int, occupied_places: int):
        """
        Создание и подготовка к работе объекта "Поезд"
        :param number_of_places: общее количество мест
        :param occupied_places: количество занятых мест
        Пример:
        >>> train = Train(100,50)
        """
        if not isinstance(number_of_places,int):
            raise TypeError("Количество всех мест должно быть целочисленным значением!")
        if number_of_places <= 0:
            raise ValueError("Количество всех мест должно быть положительным числом!")
        self.number_of_places = number_of_places
        if not isinstance(occupied_places,int):
            raise TypeError("Количество занятых мест должно быть целочисленным значением!")
        if occupied_places < 0:
            raise ValueError("Количество занятых мест должно быть неотрицательным числом!")
        if occupied_places > number_of_places:
            raise ValueError("Количество занятых мест не может превышать общее количество мест!")
        if occupied_places > number_of_places:
            raise ValueError("Количество свободных мест не может превышать общее количество мест!")
        self.occupied_places = occupied_places
        self.free_places = number_of_places - occupied_places
    def sell_tickets(self, number_of_tickets:int)->None:
        """
        Изменяет атрибуты free_places и occupied_places
        :param number_of_tickets: хранит в себе количество билетов которые хотят приобрести
        :raise ValueError: если количество билетов которое хотят купить превышает количество свободных мест
        :raise ValueError: если введенное число <= 0
        Пример:
        >>> train = Train(100, 50)
        >>> train.sell_tickets(10)
        """
        if not isinstance(number_of_tickets, int):
            raise TypeError("Количество продаваемых билетов должно быть целочисленным значением!")
        if number_of_tickets > self.free_places:
            raise ValueError("Невозможно продать такое количество билетов")
        if number_of_tickets <= 0:
            raise ValueError("Количество билетов для продажи должно быть положительным")
        ...
    def is_free_places(self)->bool:
        """
        Проверяет есть ли свободные места
        :return: есть ли места
        Пример:
        >>> train = Train(200,200)
        >>> train.is_free_places()
        """
        ...
class Cheeseburger:
    def __init__(self,number_of_burger_buns: int, number_of_burger_patties: int, number_of_cheese_slices: int):
        """
        Создание и подготовка к работе объекта "Чизбургер"
        :param number_of_burger_buns: количество булок
        :param number_of_burger_patties: количество котлет
        :param number_of_cheese_slices: количество ломтиков сыра
        Пример:
        >>> cheeseburger = Cheeseburger(2,1,1)
        """
        if not isinstance(number_of_burger_buns, int):
            raise TypeError("Количество булок должно быть целочиселенным значением!")
        if number_of_burger_buns < 0:
            raise ValueError("Количество булок не может быть отрицательным!")
        self.number_of_burger_buns = number_of_burger_buns
        if not isinstance(number_of_burger_patties, int):
            raise TypeError("Количество котлет должно быть целочиселенным значением!")
        if number_of_burger_patties < 0:
            raise ValueError("Количество котлет не может быть отрицательным!")
        self.number_of_burger_patties = number_of_burger_patties
        if not isinstance(number_of_cheese_slices, int):
            raise TypeError("Количество ломтиков сыра должно быть целочиселенным значением!")
        if number_of_cheese_slices < 0:
            raise ValueError("Количество ломтиков сыра не может быть отрицательным!")
        self.number_of_cheese_slices = number_of_cheese_slices
    def assemble_the_cheeseburger(self)->None:
        """
        Функция для сборки бургера (добавления/удаления компонентов)
        Реализация через меню ввода и конструкцию switch-case с соответсвующимим проверками ввода
        Пример:
        >>> burger = Cheeseburger(2,1,1)
        >>> burger.assemble_the_cheeseburger()
        """
        ...
    def my_cheeseburger(self)->None:
        """
        Демонстрирует собранный бургер (выводит аргументы)
        Пример:
        >>> burger = Cheeseburger(2,1,1)
        >>> burger.my_cheeseburger()
        """
class Cat:
    def __init__(self,name: str, age: int, hunger: bool):
        """
               Создание и подготовка к работе объекта "Кот"
               :param name: имя питомца
               :param age: возраст питомца
               :param hunger: голоден / сыт питомец
               Пример:
               >>> cat = Cat("Кузя",7,True)
               """
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Возраст кошки должен быть целочисленным значением!")
        if age > 38: # 38 - самый большой задокументированный возраст кошки
            raise ValueError("К сожалению, кошки столько не живут =(")
        if age < 0:
            raise ValueError("Возраст кошки не может быть отрицательным")
        self.age = age
        if not isinstance(hunger, bool):
            raise TypeError("Кошка может быть только голодной или сытой")
        self.hunger = hunger
    def feed_cat(self):
        """
        Если hunger == True то может покормить и поменать hunger = False
        Пример:
        >>> cat = Cat("Кузя",7 ,True)
        >>> cat.feed_cat()
        """
        ...
    def play_with_cat(self):
        """
        Просто играем с любимым питомцем
        Пример:
        >>> cat = Cat("Кузя",7 ,True)
        >>> cat.play_with_cat()
        """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
