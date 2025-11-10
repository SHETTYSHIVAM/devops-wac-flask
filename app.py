from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [{
    'email': 'raju@abc.in',
    'password': '1234'
},
{
    'email': 'oggy@abc.in',
    'password': '1234'
}
]

@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        for user in users:
            if (user['email'] == email and user['password'] == user['password'] == password ):
                return redirect(url_for('signup', error='User Already'))
        users.append({'email': email, 'password': password})
        return render_template('home.html')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        for user in users:
            if (user['email'] == email and user['password'] == password ):
                return render_template('home.html')
        return render_template('login.html', error='user not found')
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
