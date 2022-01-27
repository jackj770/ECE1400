# Jack Fernald
# Assignment: hw2
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on January 24, 2022
import math
import sys

height = 1
radius = 1
area_volume = "area"

helpstatement = "Hi welcome to cone calc!\nTo get started here the expected inputs:\n <height> <radius> and then 'area' or 'volume' \nfor which calculation you wish to perform"


def calc(height, radius, area_volume):
    # print(height, radius, area_volume)
    if area_volume == "area":
        temp = math.pi * radius * (radius + math.sqrt(math.pow(height, 2) + math.pow(radius, 2)))
        print("The surface %s of a cone of radius %f and height %f is: %f" % (area_volume, radius, height, temp))
    if area_volume == "volume":
        temp = math.pi * math.pow(radius, 2) * (height / 3)
        print("The %s of a cone of radius %f and height %f is: %f" % (area_volume, radius, height, temp))


try:
    if type(sys.argv[1]) != "help":
        try:
            calc(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3])
        except ValueError:
            print("Hmmm... did you mean to type that?\nHere's some help to get started!\n")
            print(helpstatement)
            exit()
    else:
        print("Displaying Help:\n")
        print(helpstatement)
        exit()
except IndexError:
    print("Hmmm... did you mean to type that?\nHere's some help to get started!\n")
    print(helpstatement)
    exit()
