from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return "Contact Page"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # handle login
        pass
    return render_template('login.html')

@app.route('/logout')
def logout():
    # handle logout
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)