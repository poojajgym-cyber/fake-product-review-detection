from flask import Flask, render_template, request, redirect, url_for, session
import random  # for dummy prediction

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy users
users = {"admin": "admin123", "user": "user123"}

# -------- Login Route --------
@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('review'))
        else:
            error = "Invalid Username or Password"
    return render_template('login.html', error=error)

# -------- Review Route --------
@app.route('/review', methods=['GET', 'POST'])
def review():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    result = ""
    if request.method == 'POST':
        product = request.form['product']
        review_text = request.form['review']
        rating = request.form['rating']

        # Dummy prediction: randomly return "Fake" or "Real"
        prediction = random.choice(["Fake", "Real"])
        result = f"Product: {product} | Rating: {rating} | Review is {prediction}"

    return render_template('review.html', result=result)

# -------- Logout Route --------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
