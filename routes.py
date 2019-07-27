from flask import flash, redirect, render_template, request, url_for, Flask

import random

app = Flask(__name__)
counter = 1
@app.route('/', methods = ['GET', 'POST'])
def home():

    # generate random for now
    generateRandomInputFile("./input/waterLevel", 0, 1001)
    generateRandomInputFile("./input/sunlightLevel", 0, 1001)
        
    # this will be constantly updating later
    water = readInputFile("./input/waterLevel")
    sunlight = readInputFile("./input/sunlightLevel")
        


    # debugging
    print(water)
    print(sunlight)


    if (request.method == "POST"):
        print("HERE!")

        # are we changing water or shade
        action = request.form["action"]

        # handle action
        # update shit here

        if (action == 'water'):
            print("WATER")
            water = updateWater()

        elif (action == 'sunlight'):
            print("SHADE")
            sunlight = updateSunlight()

    
    # return current values for water and sunlight
    return render_template('home.html', water = water, sunlight = sunlight)


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
    return render_template('home.html', water = 0, shade = 0)


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

def updateWater():
    # output signal to arduino
    generateRandomInputFile('./output/waterLevel', 0, random.randint(1,1000))
    return 100

def updateSunlight():
    generateRandomInputFile('./output/sunlightLevel', 0, random.randint(1,1000))
    # output signal to arduino
    return 100

if __name__ == "__main__":
    app.run()