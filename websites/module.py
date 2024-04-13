from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    hotels = db.relationship('Hotel', backref='city', lazy=True)

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(150))
    hotel_location = db.Column(db.String(150))
    hotel_price = db.Column(db.String(150))
    hotel_rating = db.Column(db.String(150))
    hotel_image = db.Column(db.String(150))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))  # new field for the city ID
    rooms = db.relationship('Room', backref='hotel', lazy=True)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50))
    room_type = db.Column(db.String(50))
    price = db.Column(db.Float)
    is_available = db.Column(db.Boolean, default=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    bookings = db.relationship('Booking', backref='room', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))  # new field for the room ID

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(150))
    city = db.Column(db.String(150))
    date_of_birth = db.Column(db.String(150))
    bookings = db.relationship('Booking', backref='user', lazy=True)