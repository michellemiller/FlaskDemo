# Hello world flask demo.

from flask import Flask 
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return "This is the index page."

@app.route("/hello")
def hello():
	return "Hello world!"

@app.route("/user/<username>")
def show_user_profile(username):
	#Show the user profile for that user.
	return "Username: %s" % username

@app.route("/user/<int:post_id>")
def show_post(post_id):
	# show the post with the given id, the id is an integer.
	return 'Post %d' % post_id

@app.route("/login", methods = ['GET', 'POST'])
def login():
	'''
	Shows how different HTTP methods can be handled.
	Popular ones include:
	GET; POST; HEAD; PUT; DELETE; OPTIONS
	'''
	if request.method == "POST":
		do_the_login()
	else:
		show_the_login_form()

def show_the_login_form(): pass
def do_the_login(): pass
 

#During development, flask can serve static files.
# Eg, for a file stored as static/style.css
# url_for('static', filename='style.css')




if __name__ == "main":
	app.run()