from flask import Flask, jsonify, render_template, request
from dbfunc import load_hotels_from_db, load_users_from_db


app = Flask(__name__)




@app.route('/')
def home():
    hotels = load_hotels_from_db()
    return render_template('index.html',
                            hotels=hotels)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/api/hotels')
def hotels():
    hotels = load_hotels_from_db()
    return jsonify(hotels)

@app.route('/api/users')
def users():
    users = load_users_from_db()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)