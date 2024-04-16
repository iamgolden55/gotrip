from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .module import Hotel, Room, Booking, City

views = Blueprint('views', __name__)


@views.route('/')
def home():
    hotels_with_cities = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).all()
    return render_template("home.html", user=current_user, hotels_with_cities=hotels_with_cities, rooms=Room.query.all(), bookings=Booking.query.all())

@views.route('/profile')
@login_required
def profile():
    hotels_with_cities = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).all()
    return render_template('profile.html', user=current_user, hotels_with_cities=hotels_with_cities, rooms=Room.query.all(), bookings=Booking.query.all())

@views.route('/bookings/<int:hotel_id>')
@login_required
def bookings(hotel_id):
    hotel_with_city = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).filter(Hotel.id == hotel_id).first()
    return render_template('bookings.html', user=current_user, hotel_with_city=hotel_with_city, rooms=Room.query.all(), bookings=Booking.query.all())