from flask import Flask, render_template, redirect, url_for, request, flash, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'bottle2filament_cdo_2025'
app.jinja_env.filters['strftime'] = lambda date, fmt: datetime.now().strftime(fmt)

# Fake data (will replace with SQLite later)
current_user = {"name": "Guest", "points": 0}
machine_busy = False
busy_user = ""

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
        name = request.form.get('name', '').strip()
        if not name:
            name = "Anonymous Recycler"
        session['user'] = {"name": name, "points": 170}
        session['busy'] = False
        flash(f"Mabuhay, {name}!", "success")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('landing'))
    return render_template('home.html', user=session['user'], busy=machine_busy, busy_user=busy_user)

@app.route('/recycle')
def recycle():
    if 'user' not in session:
        return redirect(url_for('landing'))
    global machine_busy, busy_user
    if machine_busy:
        flash("Machine is busy! Please wait.", "warning")
        return redirect(url_for('home'))
    machine_busy = True
    busy_user = session['user']['name']
    return render_template('recycle.html', user=session['user'])

@app.route('/finish_recycle')
def finish_recycle():
    global machine_busy, busy_user
    machine_busy = False
    busy_user = ""
    session['user']['points'] += 30
    flash("+30 points! Salamat sa pag-recycle!", "success")
    return redirect(url_for('home'))

@app.route('/shop')
def shop():
    if 'user' not in session:
        return redirect(url_for('landing'))
    rewards = [
        {"id":1, "name":"CDO Keychain", "points":80, "stock":5, "img":"keychain.jpg"},
        {"id":2, "name":"Phone Stand", "points":120, "stock":3, "img":"stand.jpg"},
        {"id":3, "name":"Cable Organizer", "points":50, "stock":10, "img":"organizer.jpg"},
        {"id":4, "name":"USTP Badge", "points":100, "stock":8, "img":"badge.jpg"},
    ]
    return render_template('shop.html', rewards=rewards, user=session['user'])

@app.route('/redeem/<int:item_id>')
def redeem(item_id):
    costs = {1:80, 2:120, 3:50, 4:100}
    names = {1:"CDO Keychain", 2:"Phone Stand", 3:"Cable Organizer", 4:"USTP Badge"}
    if session['user']['points'] >= costs[item_id]:
        session['user']['points'] -= costs[item_id]
        return render_template('ticket.html', item=names[item_id], user=session['user'])
    else:
        flash("Kulang ang points!", "danger")
        return redirect(url_for('shop'))

@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('landing'))
    return render_template('profile.html', user=session['user'])

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/logout')
def logout():
    session.clear()
    global machine_busy, busy_user
    machine_busy = False
    busy_user = ""
    flash("Salamat sa pagbisita!", "info")
    return redirect(url_for('landing'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)