from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .module import Hotel, Room, Booking, City

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
    hotels_with_cities = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).all()
    print(hotels_with_cities)
    return render_template('profile.html', user=current_user, hotels_with_cities=hotels_with_cities, rooms=Room.query.all(), bookings=Booking.query.all())
    