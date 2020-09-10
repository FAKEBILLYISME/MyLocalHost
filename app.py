from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user = request.form["nm"]
		session["user"] = user
		return redirect(url_for("user", usr=user))
	else:
		return render_template('login.html')

@app.route("/user")
def user(usr):
	return f"<h1></h1>"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=60)