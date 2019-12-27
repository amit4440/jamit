# importing flask module fro
from flask import Flask, render_template,request

# initializing a variable of Flask
app = Flask(__name__)


# decorating index function with the app.route with url as /login
@app.route('/login')
def index():
    return render_template('login.html')


@app.route('/SJ',  methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        return render_template('success.html', email=email)
    else:
        pass

@app.route("/")
def hello():
    return "Welcome to the World of FLASK...!!!"

if __name__ == "__main__":
    app.run( host='localhost',debug=True, port=5000)