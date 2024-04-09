from flask import Flask, jsonify, render_template, request
from dbfunc import load_hotels_from_db, load_user_from_db, load_room_from_db
#connection to DB



app = Flask(__name__)



@app.route('/testlogin')
def testlogin():
    return render_template('testlogin.html')
@app.route('/testregister')
def testregister():
    return render_template('testereg.html')

@app.route('/')
def home():
    hotels = load_hotels_from_db()
    rooms = load_room_from_db()
    return render_template('index.html',
                            hotels=hotels,
                            rooms=rooms)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')
@app.route('/api/hotels')
def hotels():
    hotels = load_hotels_from_db()
    return jsonify(hotels)

@app.route('/api/users')
def users():
    users = load_user_from_db()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)