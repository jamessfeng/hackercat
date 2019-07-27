from flask import flash, redirect, render_template, request, url_for, Flask

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	return render_template('home.html')





if __name__ == "__main__":
	app.run()