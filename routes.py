from flask import flash, redirect, render_template, request, url_for, Flask
from flask_socketio import SocketIO

import random

app = Flask(__name__)
counter = 1
@app.route('/', methods = ['GET', 'POST'])
def home():
    global counter
    counter += 1

    # generate random for now
    generateRandomInputFile("./input/waterLevel", 0, 1001)
    generateRandomInputFile("./input/shadeLevel", 0, 1001)
        
    # this will be constantly updating later
    water = readInputFile("./input/waterLevel")
    shade = readInputFile("./input/shadeLevel")
        
    print(water)
    print(shade)


    if (request.method == "POST"):
        # water the plant with x water
        # shade the plant with x shade

        waterChange = request.form['nWater']
        shadeChange = request.form['nShade']




        # update shit here

    return render_template('home.html', water = water, shade = shade)


@app.route('/', methods = ['GET', 'POST'])
def profile():
    pass


@app.route('/', methods = ['GET', 'POST'])
def battle():
    pass


@app.route('/', methods = ['GET', 'POST'])
def shop():
    pass



def readInputFile(fileName):

    file = open(fileName, 'r')
    content = file.read().strip() # remove leading/trailing spaces
    content = content.split("\n") # split to calculate avg

    return average(content)


def generateRandomInputFile(fileName, low, high):
    file = open(fileName, 'w')

    for _ in range(random.randint(0, 100)):
        file.write(str(random.randint(low,high)) + "\n")
    # testing function because i don't have the input values yet

def average(arr):
    if (len (arr) == 0):
        return 0

    total = 0
    for n in arr:
        total += int(n) 

    return total/len(arr)


if __name__ == "__main__":
    app.run()