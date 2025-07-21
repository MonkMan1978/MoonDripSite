import os
import logging
import requests
from flask import Flask, render_template, request, redirect, url_for, flash

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
print("App is starting...")
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SESSION_SECRET", "dev_secret_key_change_in_production")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/education.html")
def education():
    return render_template("education.html")

@app.route("/join.html")
def join():
    return render_template("join.html")

@app.route("/sponsors.html")
def sponsors():
    return render_template("sponsors.html")

@app.route("/calculator.html")
def calculator():
    return render_template("calculator.html")

@app.route("/join", methods=["POST"])
def join_post():
    email = request.form.get("email", "").strip()
    if not email:
        flash("Please enter a valid email address.")
        return redirect(url_for("join"))

    # Send to ConvertKit
    try:
        api_key = os.environ.get("CONVERTKIT_API_KEY")
        form_id = os.environ.get("CONVERTKIT_FORM_ID")
        response = requests.post(
            f"https://api.convertkit.com/v3/forms/{form_id}/subscribe?api_key={api_key}",
            json={"email": email},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        flash("Thanks for signing up! You’re officially part of the MoonDrip orbit 🚀")
    except Exception as e:
        logging.error(f"ConvertKit signup failed: {e}")
        flash("There was a problem signing you up. Please try again later.")

    return redirect("/join.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
