# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for enemy in dragon_list:
        if isinstance(enemy,Dragon):
            print('Вышел', enemy._color, 'дракон!')
            while enemy.is_alive() and hero.is_alive():
                print('Вопрос:', enemy.question())
                answer = annoying_input_int('Ответ:')

                if enemy.check_answer(answer):
                    hero.attack(enemy)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    enemy.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if enemy.is_alive():
                break
            print('Дракон', enemy._color, 'повержен!\n')
        elif isinstance(enemy,troll):
            print('Вышел',enemy._color,'Тролль!')
            while enemy.is_alive() and hero.is_alive():
                print('Вопрос:', enemy.question())
                answer = annoying_input_int('Ответ:')

                if enemy.check_answer(answer):
                    hero.attack(enemy)
                    print('Верно! \n** тролль кричит от боли **')
                else:
                    enemy.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if enemy.is_alive():
                break
            print('Тролль', enemy._color, 'повержен!\n')
        else:
            print('VAS UKUSILI')
            hero._health-=10

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'монстров!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
