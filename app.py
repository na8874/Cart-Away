from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def login():
  return render_template('login.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/signup')
def signup():
  return render_template('signup.html')


@app.route('/clothe')
def clothe():
  return render_template('clothe.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/index1', methods=['GET', 'POST'])
def index1():
  if request.method == 'POST':
    a = request.form['username']
    b = request.form['Password']

    print(a, b)
    if (a == "nikhil@gmail.com" and b == "12345"):
      return render_template('index.html')
    else:
      return render_template('login.html',
                             error='Enter Correct Login Credentials')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
