from random import randint
import math

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class Creature:
    def __init__(self,x,y,speed,sight):
        self.x = x
        self.y = y
        self.speed = speed
        self.sight = sight

    def find_food(self, foodlist):
        for food in foodlist:
            if ((food.x-self.x)**2+(food.y-self.y)**2)**0.5<self.sight:
                self.x = food.x
                self.y = food.y
                return True
        return False
    def move(self,foodlist):
        if not(self.find_food(foodlist)):
            theta = randint(0,359)
            self.x+=self.speed*math.cos(math.pi*theta/180.)
            self.y+=self.speed*math.sin(math.pi*theta/180.)
            if self.x>100:
                self.x = 100
            elif self.x<-100:
                self.x = -100
            elif self.y>100:
                self.y = 100
            elif self.y<-100:
                self.y = -100

class Food:
    def __init__(self,x,y):
        self.x = x
        self.y = y

foodlist = [Food(randint(-100,100),randint(-100,100)) for i in range(50)]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

creaturelist = [Creature(-100,randint(-100,100),20,10) for i in range(10)]
while True:
    ax.clear()
    ax.scatter([creature.x for creature in creaturelist],[creature.y for creature in creaturelist], color='r')
    ax.scatter([food.x for food in foodlist],[food.y for food in foodlist],color='b')
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    plt.pause(0.1)
    for creature in creaturelist:
        creature.move(foodlist)
        for food in foodlist:
            if creature.x==food.x and creature.y == food.y:
                foodlist.remove(food)
    foodlist.extend([Food(randint(-100,100),randint(-100,100)) for i in range(1)])


plt.show()
