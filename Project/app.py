from flask import *
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/BodyBuilding"
mongo = PyMongo(app)
app.secret_key = "ali12345"
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['POST'])
def register():
      email = request.form['email']
      password = request.form['pass']
      name = request.form['name']
      lastName = request.form['lastName']
      mongo.db.Users.insert({'name': name, 'password': password , 'lastName':lastName ,'email' : email })
      return render_template('index.html')
#
#
@app.route('/checklogin', methods=['POST'])
def checklogin():
      email = request.form['email']
      password = request.form['pass']
      users = mongo.db.Users
      user = users.find_one({'email': email, 'password': password})
      if user is not None:
         session['email'] = email
         return render_template('index.html')
      else:
         return render_template('login.html')

@app.route('/programs')
def programs():
    if session.get('email') is not None:
      return render_template('programs.html')
    return render_template('login.html')
@app.route('/programs/program')
def program():
    if session.get('email') is not None:
      return render_template('program.html')
    return render_template('login.html')

@app.route('/about_us')
def about():
    if session.get('email') is not None:
      return render_template('aboutus.html')
    return render_template('login.html')
#
@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
