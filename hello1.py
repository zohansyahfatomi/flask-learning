from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!1!</p>"

#route
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

#variable rules
#@app.route('/user/<username>')
#def show_user_profile(username):
    #show the user profile for that user
#    return f'User {escape(username)}' #username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return f'Post {post_id}' #integer 

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}' #path

'''
string : (default) accepts any text without slash
int : accepts positive integers
float : accepts positive floating point values 
path : like string but also accepts slashes
uuid : accepts UUID strings
'''

#Unique URLs/Redirection Behavior
@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

#url building
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    #show the user profile for that user
    return f'{escape(username)} profile' 

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile',username = 'John Doe'))

