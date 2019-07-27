from flask import flash, redirect, render_template, request, url_for, Flask

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('base.html')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)



if __name__ == "__main__":
	app.run()