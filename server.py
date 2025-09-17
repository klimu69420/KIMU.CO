from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Change this to your Gmail + App Password (not your normal Gmail pass)
ADMIN_EMAIL = "yourgmail@gmail.com"
ADMIN_PASS = "your_app_password_here"  

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    pack = data.get("pack")
    message = data.get("message")

    # Email body
    msg = MIMEMultipart()
    msg["From"] = ADMIN_EMAIL
    msg["To"] = ADMIN_EMAIL
    msg["Subject"] = f"New Registration from {name}"

    body = f"""
    Name: {name}
    Email: {email}
    Pack: {pack}
    Message: {message}
    """
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(ADMIN_EMAIL, ADMIN_PASS)
            server.send_message(msg)
        return jsonify({"message": "✅ Registration sent! Check your Gmail."})
    except Exception as e:
        return jsonify({"message": f"❌ Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
