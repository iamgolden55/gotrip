from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from . import db
from .module import Hotel, Room, Booking, City
from flask import request, redirect, url_for


views = Blueprint('views', __name__)


@views.route('/')
def home():
    hotels_with_cities = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).all()
    return render_template("home.html", user=current_user, hotels_with_cities=hotels_with_cities, rooms=Room.query.all(), bookings=Booking.query.all())

@views.route('/404')
def error_404():
    return render_template('404.html')

@views.route('/profile')
@login_required
def profile():
    hotels_with_cities = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).all()
    return render_template('profile.html', user=current_user, hotels_with_cities=hotels_with_cities, rooms=Room.query.all(), bookings=Booking.query.all())

@views.route('/bookings/<int:hotel_id>')
@login_required
def bookings(hotel_id):
    hotel_with_city = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).filter(Hotel.id == hotel_id).first()
    rooms = Room.query.filter_by(hotel_id=hotel_id).all()
    return render_template('bookings.html', user=current_user, hotel_with_city=hotel_with_city, rooms=rooms, bookings=Booking.query.all())

@views.route('/hotelpage/<int:hotel_id>')
def hotelpage(hotel_id):
    hotel_with_city = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).filter(Hotel.id == hotel_id).first()
    return render_template('hotelpage.html', user=current_user, hotel_with_city=hotel_with_city, rooms=Room.query.all(), bookings=Booking.query.all())



@views.route('/hotel_info/<int:hotel_id>')
def hotel_info(hotel_id):
    hotel_with_city = db.session.query(Hotel, City).join(City, Hotel.city_id == City.id).filter(Hotel.id == hotel_id).first()
    if hotel_with_city is None:
        return jsonify({'error': 'Hotel not found'}), 404
    hotel, city = hotel_with_city
    return jsonify({
        'hotel_name': hotel.hotel_name,
        'hotel_image': hotel.hotel_image,
        'city_name': city.name,
        # Add any other fields you need
    })
@views.route('/booking', methods=['GET', 'POST'])
@login_required
def booking():
    if request.method == 'POST':
        
        room_id = request.form.get('room_id')
        user_id = current_user.id
        check_in_date = request.form.get('checkInDate')
        check_out_date = request.form.get('checkOutDate')

        new_booking = Booking(room_id=room_id, user_id=user_id, check_in_date=check_in_date, check_out_date=check_out_date)
        db.session.add(new_booking)
        db.session.commit()

        return redirect(url_for('views.profile'))  # Redirect to the profile page after booking

    # If the method is GET, render the booking page
    return render_template('bookings.html')

@views.route('/success')
@login_required
def success():
    return render_template('success.html')