from flask import Blueprint, render_template, request, flash
from .module import User
from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "Logout"

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
            new_user = User(username=username, email=email, password=password1, full_name=firstName, city=city, date_of_birth=Dob)
            flash("Account created", category='success')
            # Here you should also add the code to actually create the account
            # Then you might want to redirect the user to the login page or the account page
            # return redirect(url_for('login'))

    return render_template("sign-up.html")