from flask import flash, redirect, render_template, request, url_for, Flask
import csv
import random
import xlrd
import pandas as pd 
import serial as s
import math

app = Flask(__name__)
counter = 1
    
optimalSunlight = 80
optimalWater = 90

@app.route('/', methods = ['GET', 'POST'])
def home():

    # generate random for now
    # generateRandomInputFile("./input/waterLevel", 0, 1001)
    # generateRandomInputFile("./input/sunlightLevel", 0, 1001)



    # file = '../../../../../Program Files (x86)/Parallax Inc/PLX-DAQ/PLX-DAQ.xls'
    # file = '../../../../../Program Files (x86)/Parallax Inc/PLX-DAQ/test.xlsx'

    file = "input/result.xls"
    print("STARTING TO READ...")
    df = pd.read_excel(file)


    water = df['Water']
    sunlight = df['Sunlight']

    print(water)
    print(sunlight)

    if len(water) == 0:
        water = 0
        print("CANNOT DETECT WATER")
    else:
        water = df['Water'][len(water) - 2]

    if len(sunlight) == 0:
        sunlight = 0
        print("CANNOT DETECT WATER")
    else:
        sunlight = df['Sunlight'][len(sunlight) - 2]

    print("made it here!")
    if (request.method == "POST"):
        print("HERE!")

        # are we changing water or shade
        action = request.form["action"]

        # handle action
        # update shit here

        if (action == 'water'):
            print("WATER")
            # water = changeWater()

        elif (action == 'sunlight'):
            print("SHADE")
            # sunlight = changeSunlight()



    updateWater = 0
    updateSunlight = 0

    if abs(optimalWater - water) > 25:
        updateWater = 1

    if abs(optimalSunlight - sunlight) > 25:
        updateSunlight = 1

    # return current values for water and sunlight
    return render_template('home.html', water = water, sunlight = sunlight,\
                            optimalWater = optimalWater, optimalSunlight = optimalSunlight, \
                            updateWater = updateWater, updateSunlight = updateSunlight)


@app.route('/', methods = ['GET', 'POST'])
def profile():
    pass


@app.route('/', methods = ['GET', 'POST'])
def battle():
    pass


@app.route('/', methods = ['GET', 'POST'])
def shop():
    pass

@app.route('/update', methods = ['GET', 'POST'])
def update():
    print("UPDATING!")
    return render_template('home.html', water = 0, shade = 0,)


def readInputFile(fileName):

    file = open(fileName, 'r')
    content = file.read().strip() # remove leading/trailing spaces
    content = content.split("\n") # split to calculate avg
    
    return average(content)


def generateRandomInputFile(fileName, low, high):
    file = open(fileName, 'w')

    for _ in range(random.randint(1, 100)):
        file.write(str(random.randint(low,high)) + "\n")
    # testing function because i don't have the input values yet

def average(arr):
    if (len (arr) == 0):
        return 0

    total = 0
    for n in arr:
        total += int(n) 

    return total//len(arr)

def changeWater():
    # output signal to arduino
    generateRandomInputFile('./output/waterLevel', 0, random.randint(1,100))
    return optimalWater

def changeSunlight():
    generateRandomInputFile('./output/sunlightLevel', 0, random.randint(1,100))
    # output signal to arduino
    return optimalSunlight

if __name__ == "__main__":

    app.run()