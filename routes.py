from flask import flash, redirect, render_template, request, url_for, Flask

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        # if request.form['u_name] == 'Do Something':
        #     print("asdfasdf")
        #     return return_template("garden.html")
        # elif request.form['submit_button'] == 'Do Something Else':

        #     return "2"
        amount = request.form["amount"]
        # iq = request.form["iq"]
        print(amount + "POST REQUEST")


    return render_template('home.html')





if __name__ == "__main__":
	app.run()