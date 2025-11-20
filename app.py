import calendar
import datetime
import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, session
from flask_wtf import CSRFProtect
from models import Contact, Event, Message, Profile, Security, Storage, User
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
    if request.method == "POST":
        security = Security()
        fullname = security.validate_name(request.form.get("name"))
        email = security.validate_email(request.form.get("email"))
        password = security.validate_password(request.form.get("password"))
        user = User(fullname=fullname, email=email, password=password)
        user.register(db_engine)
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


@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        security = Security()
        name = security.validate_name(request.form.get("name"))
        email = security.validate_email(request.form.get("email"))
        company = request.form.get("company")
        title = security.validate_name(request.form.get("title"))
        mobile = security.validate_mobile(request.form.get("mobile"))
        tag = request.form.get("tag")
        note = request.form.get("note")
        user_id = 2
        contact = Contact(
            fullname=name,
            email=email,
            company=company,
            title=title,
            mobile=mobile,
            tag=tag,
            note=note,
            user_id=user_id,
        )
        contact.add_contact(db_engine)
    return render_template("contacts.html")


@app.route("/contacts/edit/<contact_id>")
def edit_contact():
    pass


@app.route("/contacts/remove/<contact_id>")
def remove_contact(contact_id):
    pass


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


@app.route("/calendar/add/event", methods=["GET", "POST"])
def add_event():
    calendar_event = Event(
        event_id=2, user_id=2, venue="1234 Somewhere Dr Neverland, Ca", priority="high"
    )
    event = calendar_event.edit_event(db_engine)
    print(event)
    return {"status": 200}


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
