from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!1!</p>"

#route
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

#variable rules
@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}'

'''
string : (default) accepts any text without slash
int : accepts positive integers
float : accepts positive floating point values 
path : like string but also accepts slashes
uuid : accepts UUID strings
'''






