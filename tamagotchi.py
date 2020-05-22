import schedule
import time
import termcolor
from threading import Thread


class Pet:
    def __init__(self, name, type, age, hunger, fun, clean, health):
        self.name = name
        self.type = type
        self.age = age
        self.hunger = hunger
        self.fun = fun
        self.clean = clean
        self.health = health


    def play(self):
        type_of_game = input('What type of game do you want to play: short or long? ').lower()
        if type_of_game == 'long':
            print('Playing with {}...'.format(self.name))
            time.sleep(10)
            print(termcolor.colored(f'{self.name}:', 'grey', 'on_yellow') + ' I really like playing with you!')
            print('Fun +25 points')
            self.fun += 25
        elif type_of_game == 'short':
            print('Playing with {}...'.format(self.name))
            time.sleep(5)
            print(termcolor.colored(f'{self.name}:', 'grey', 'on_yellow') + ' I really like playing with you!')
            print('Fun +10 points')
            self.fun += 10
        self.indicate_parameters()


    def give_eat(self):
        food = input('What eat do you want to give {}. Berry or bread? '.format(self.name)).lower()
        if food == 'bread':
            self.hunger += 30
            print(termcolor.colored(f"{self.name}:", 'grey', 'on_yellow') + " It's so nourishing. Thank You.")
            print('Hunger +30 points')
        elif food == 'berry':
            self.hunger += 15
            self.fun += 15
            print(termcolor.colored(f"{self.name}:", 'grey', 'on_yellow') + " It's so delicious. Thank You!")
            print('Hunger +15 points, Fun +15 points')
        else:
            print(termcolor.colored(f"{self.name}:", 'grey', 'on_yellow') + " I don\'t want it. Give me bread or berry")
            self.give_another_eat()
        self.indicate_parameters()


    def give_another_eat(self):
        food = input('What eat do you want to give {}. Berry or bread? '.format(self.name)).lower()
        if food == 'bread':
            self.hunger += 30
            print(termcolor.colored(f"{self.name}:", 'grey', 'on_yellow') + " It's so nourishing. Thank You.")
        elif food == 'berry':
            self.hunger += 15
            self.fun += 15
            print(termcolor.colored(f"{self.name}:", 'grey', 'on_yellow') + " It's so delicious. Thank You!")
        else:
            print(termcolor.colored(f"{self.name}:", 'grey', 'on_yellow') + " I don\'t want it. Give me bread or berry")
            self.give_another_eat()


    def indicate_parameters(self):
        print('Hunger: {}, Fun: {}, Clean: {}, Health: {}'.format(self.hunger, self.fun, self.clean, self.health))
        print('')


    def actions(self):
        do = input('What do you want to do? ').lower().split()
        for i in do:
            if i == 'feed':
                self.give_eat()
                self.actions()
            elif i == 'play':
                self.play()
                self.actions()
        self.dont_understand()


    def dont_understand(self):
        print(f'I don\'t understand you. Do u want to play with your {self.type} or feed him?')
        print('')
        self.actions()


pikachu = Pet('Pikachu', 'pokemon', 0, 70, 70, 70, 100)

def lowing_parameters():
    pikachu.hunger -= 3
    pikachu.fun -= 3
    pikachu.clean -= 3


def run():
    schedule.every(10).seconds.do(lowing_parameters)

    while True:
        schedule.run_pending()
        time.sleep(1)


game_time = Thread(target=run)
game_time.start()
pikachu.actions()


