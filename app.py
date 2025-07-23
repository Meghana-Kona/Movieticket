from flask import Flask, render_template, request, redirect
import sqlite3
import os
app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        movie TEXT,
        date TEXT,
        time TEXT,
        persons INTEGER
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    movies = [
        {"title": "Jurassic World Rebirth", "image": "https://dx35vtwkllhj9.cloudfront.net/universalstudios/jurassic-world-rebirth/images/regions/us/updates1/header.jpg"},
        {"title": "Demon Slayer:Infinity Castle", "image": "https://platform.polygon.com/wp-content/uploads/sites/2/2025/03/Demon-Slayer_-Kimetsu-no-Yaiba-Infinity-Castle-Theatrical-Date-Poster-US.jpg?quality=90&strip=all&crop=0,17.654333274357,100,47.180938900684"},
        {"title": "HIT3", "image": "https://images.moneycontrol.com/static-mcnews/2025/05/20250501173219_hit-3-bxo.jpg?impolicy=website&width=770&height=431"},
    ]
    return render_template('index.html', movies=movies)

@app.route('/book/<movie>')
def book(movie):
    return render_template('book.html', movie=movie)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    movie = request.form['movie']
    date = request.form['date']
    time = request.form['time']
    persons = request.form['persons']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO bookings (name, movie, date, time, persons) VALUES (?, ?, ?, ?, ?)",
              (name, movie, date, time, persons))
    conn.commit()
    conn.close()
    return redirect('/tickets')

@app.route('/tickets')
def tickets():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookings")
    bookings = c.fetchall()
    conn.close()
    return render_template('tickets.html', bookings=bookings)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM bookings WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/tickets')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
