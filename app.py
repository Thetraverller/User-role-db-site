from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to validate user credentials
def validate_login(username, password):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Fetch user with the given username and password from the database
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    conn.close()

    return user

# Function to get all users from the database
def get_all_users():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Fetch all users from the database
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    conn.close()

    return users

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate user credentials
        user = validate_login(username, password)

        if user:
            users = get_all_users()
            return render_template('dashboard.html', users=users)
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
