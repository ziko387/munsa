from django.contrib.admin import display


class Person:
    def __init__(self,name,_age,__salary):
        self.name = name
        self._age = _age
        self.__salary = __salary
    def display_info(self):
        print(f"name{self.name} age{self._age} salary{self.__salary}")

        man1=Person("juma",_age=24,__salary=20000)
        man2=Person("alex",_age=23,__salary=20000)
        man1.display_info()
        man2.display_info()

        print(man1)
        print(man2)












