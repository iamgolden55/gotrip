from . import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .module import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.profile'))
            else:
                flash("Incorrect password, try again", category='error')
        else:
            flash("Username does not exist", category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email_address')
        firstName = request.form.get('full_name')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')
        city = request.form.get('city')
        Dob = request.form.get('date_of_birth')

        if username is None or len(username) < 2:
            flash("Username must be greater than 1 character", category='error')
            return render_template("sign-up.html")
        elif email is None or len(email) < 6:
            flash("Email must be greater than 6 characters", category='error')    
            return render_template("sign-up.html")
        elif firstName is None or len(firstName) < 2:
            flash("First name must be greater than 1 character", category='error')
            return render_template("sign-up.html")
        elif password1 is None or password2 is None or password1 != password2:
            flash("Passwords don't match", category='error')
            return render_template("sign-up.html")
        elif password1 is None or len(password1) < 7:
            flash("Password must be at least 7 characters", category='error')
            return render_template("sign-up.html")
        elif city is None or len(city) < 2:
            flash("City must be greater than 1 character", category='error')
            return render_template("sign-up.html")
        elif Dob is None or int(Dob.split('-')[0]) >= 2018:
            flash("Enter a valid year", category='error')
            return render_template("sign-up.html")
        else:
            # Check if a user with the given username already exists
            user = User.query.filter_by(username=username).first()
            if user:
                flash('Username already exists.', category='error')
                return render_template("sign-up.html")
            else:
                new_user = User(username=username, email=email, password=generate_password_hash(password1, method='scrypt'), full_name=firstName, city=city, date_of_birth=Dob)
                db.session.add(new_user)
                db.session.commit()
                login_user(user, remember=True)
                flash("Account created", category='success')
                return redirect(url_for('views.home'))
                # Here you should also add the code to actually create the account
                # Then you might want to redirect the user to the login page or the account page
                # return redirect(url_for('login'))

    return render_template("sign-up.html", user=current_user)