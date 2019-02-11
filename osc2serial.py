import serial as s
import color_consts as cc
import random as r
import time

ser = s.Serial('/dev/ttyACM0', 9600)

ser.write(b"test")


def manual():
    #wait for user input and repeat
    while(True):
        #usr_red, usr_green, usr_blue = collect_usr_input()
        #sendRGB((usr_red, usr_green, usr_blue))

        #if (input() == "red"):
            #sendRGB(cc.RED)
        red = r.randint(0, 255)
        green = r.randint(0, 150)
        blue = r.randint(0, 200)

        sendRGB((red, green, blue))

        time.sleep(2)



def sendRGB(rgb):

    #convert numbers to three-digit format
    r, g, b = str(rgb[0]), str(rgb[1]), str(rgb[2])

    while len(r) < 3:
        r = "0" + r
    while len(g) < 3:
        g = "0" + g
    while len(b) < 3:
        b = "0" + b

    ser.write(("RGB: " + r + " " + b + " " + g).encode())
    print("sent red " + r + ", green " + g + " and blue " + b)


def collect_usr_input():
    while True:
        usr_red = input("red: ")
        if int(usr_red) <= 255 and int(usr_red) >= 0:
            break
    while True:
        usr_green = input("green: ")
        if int(usr_green) <= 255 and int(usr_green) >= 0:
            break
    while True:
        usr_blue = input("blue: ")
        if int(usr_blue) <= 255 and int(usr_blue) >= 0:
            break

    return usr_red, usr_green, usr_blue


manual()