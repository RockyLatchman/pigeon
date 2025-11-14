import calendar
import datetime
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, session
from flask_wtf import CSRFProtect
from models import Account, Contact, Event, Message, Storage
from sqlmodel import Session, create_engine

load_dotenv(".env")

app = Flask(__name__)
app.config["DATABASE_URL"] = os.environ.get("DATABASE_URL")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
db_engine = create_engine(app.config["DATABASE_URL"], echo=True)
csrf_token = CSRFProtect(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/signout")
def signout():
    return render_template("signout.html")


@app.route("/inbox")
def inbox():
    return render_template("inbox.html")


@app.route("/inbox/send")
def send_message():
    pass


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/calendar")
def pigeon_calendar():
    user_calendar = calendar.HTMLCalendar(firstweekday=0)
    current_date = datetime.datetime.today()
    return render_template(
        "calendar.html",
        current_day=current_date.strftime("%A"),
        current_date=current_date.strftime("%d"),
        cal=user_calendar.formatmonth(current_date.year, current_date.month),
    )


@app.route("/calendar/event", methods=["POST"])
def calendar_event():
    # remove or add event to calendar
    pass


@app.route("/storage")
def storage():
    return render_template("storage.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/tags/<color>")
def tag(color):
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5555)
