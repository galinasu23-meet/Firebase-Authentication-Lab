from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {

    "apiKey": "AIzaSyBYYYa-SNLzgCzictVNPG9-wHMjft_ewkw",

    "authDomain": "gali-2be0b.firebaseapp.com",

    "databaseURL": "https://gali-2be0b-default-rtdb.europe-west1.firebasedatabase.app",

    "projectId": "gali-2be0b",

    "storageBucket": "gali-2be0b.appspot.com",

    "messagingSenderId": "1016207388612",

    "appId": "1:1016207388612:web:ba459a9e5a20e7d51b3e91",

    "measurementId": "G-6T0048M311",

    "databaseURL": "https://gali-2be0b-default-rtdb.europe-west1.firebasedatabase.app/"

}

firebase= pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('yourpage'))
        except:
            error = "fail"
    return render_template("signin.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
           login_session['user'] = auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
        except:
             error = "Authentication failed"
    return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


@app.route('/yourpage', methods=['GET', 'POST'])
def yourpage():
    return render_template("yourpage.html")


@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))




if __name__ == '__main__':
    app.run(debug=True)