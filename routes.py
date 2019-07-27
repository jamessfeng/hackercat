from flask import flash, redirect, render_template, request, url_for, Flask
import app.application

a = app.application.app

@app.route('/')
def home():
    return 'home'


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# if __name__ == '__main__':
#     app.run()


# def run():
# 	app.run()