from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Анатолий'}
    return render_template('index.html', title='Home', user=user)
    

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
    
@app.route('/post/<username>/<int:age>')
def show_post(username, age):
  return 'Возраст %s - %d' %(username, age)
