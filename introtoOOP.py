# OOP
import pygame
import random

lst = []
for i in range(6):
    number = random.randint(1, 100)
    lst.append(number)


class Sort:
    def __init__(self, lst, model):
        self.lst = lst
        self.model = model
        self.sorted = False
    def output(self):
        print(self.lst)

    #def swap(i, j):
        #self.distance += newDistance
    #def comparison(i,j):



sorting = Sort(lst, "Bubble")
print(sorting)


class Algorithm(Sort):

    def Step(self, newload):
        pass
