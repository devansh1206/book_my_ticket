from flask import Flask, render_template, request, url_for, redirect, session
app = Flask(__name__)
'''app.config["SECRET_KEY"]="dev1206"'''



@app.route('/', methods=["GET", "POST"])
def home():
    movies = [["Brahmastra","static/img/Brahmastra.jfif"], ["Chup", "static/img/Chup.jfif"], ["Sita-Ram", "static/img/Sita-Ramam.jfif"]]
    return render_template('index.html',li = movies)

'''app.route('/select_movie')
def select_mov(city_name):
    return render_template("select_movie.html", city = city_name)

app.route('/select_seat')
def select_seat(number):
    return render_template("select_seat.html", no = number)

app.route('/checkout')
def checkout(amount):
    return render_template("checkout.html", amount = amount)'''

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        debug = True,
        port = 8080
    )
