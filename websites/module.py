from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(50), unique=True)
    hotels = db.relationship('Hotel', backref='city', lazy=True)

class Hotel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(150))
    hotel_location = db.Column(db.String(150))
    hotel_price = db.Column(db.String(150))
    hotel_rating = db.Column(db.String(150))
    hotel_image = db.Column(db.String(150))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    rooms = db.relationship('Room', backref='hotel', lazy=True)

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50))
    room_type = db.Column(db.String(50))
    price = db.Column(db.Float)
    is_available = db.Column(db.Boolean, default=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))
    bookings = db.relationship('Booking', backref='room', lazy=True)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(512))
    full_name = db.Column(db.String(150))
    city = db.Column(db.String(150))
    date_of_birth = db.Column(db.String(150))
    bookings = db.relationship('Booking', backref='user', lazy=True)