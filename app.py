from flask import Flask, render_template, redirect, url_for, request, flash, session
import os

app = Flask(__name__)
app.secret_key = 'bottle2filament_cdo_2025'

# Fake login for testing
@app.before_request
def captive_portal_redirect():
    if request.path in ['/generate_204', '/hotspot-detect.html']:
        return redirect(url_for('landing'))

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous').strip()
        if not name:
            name = "Anonymous Recycler"
        session['user'] = {"name": name, "points": 150}
        flash(f"Welcome, {name}!", "success")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('landing'))
    return render_template('home.html', user=session['user'])

@app.route('/recycle')
def recycle():
    if 'user' not in session:
        return redirect(url_for('landing'))
    return render_template('recycle.html')

@app.route('/shop')
def shop():
    rewards = [
        {"id":1, "name":"CDO Keychain", "points":80, "stock":5},
        {"id":2, "name":"Phone Stand", "points":120, "stock":3},
        {"id":3, "name":"Cable Organizer", "points":50, "stock":10},
    ]
    return render_template('shop.html', rewards=rewards)

@app.route('/profile')
def profile():
    return render_template('profile.html', user=session.get('user', {}))

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Salamat sa pag-recycle!", "info")
    return redirect(url_for('landing'))

if __name__ == '__main__':
    app.run(debug=True)