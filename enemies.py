# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,x)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class trollwarlord(troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'воинственный'

    def question(self):
        x = randint(1,5)
        self.__quest = "Угадаешь число от 1 до 5, путник?"
        self.set_answer(x)
        return self.__quest


class stupidtroll(troll):
    def __init__(self):
        self._health = 150
        self._attack = 20
        self._color = 'глупый'

    def question(self):
        x = randint(1,100)
        m=1
        for i in range(2,x//2):
            if x % i==0:
                m=0
                break
        self.__quest = "Простое ли число "+str(x)+"? Введи 1,если да, или 0,если нет"
        self.set_answer(m)
        return self.__quest


class clevertroll(troll):
    def __init__(self):
        self._health = 180
        self._attack = 50
        self._color = 'умный'

    def question(self):
        x = randint(3,30)
        chislo=x
        i=2
        otvet=''
        while i<=chislo//2:
            if x%i==0:
                otvet+=str(i)
                x=x/i
            else:
                i=i+1
        self.__quest = str(otvet)+"Дружок, разложи-ка мне число "+str(chislo)+ " на множители!Вывеdi bez probelov v poryadke vozrastaniya"
        self.set_answer(otvet)
        return self.__quest
class rat(Enemy):
    pass
#FIXedME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [rat,trollwarlord,stupidtroll,BlackDragon,RedDragon, GreenDragon] #Clevertroll isn't working yet