import calendar
import datetime
import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, flash, jsonify, render_template, request, session
from flask_wtf import CSRFProtect
from models import Contact, Event, Message, Security, Storage, User
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
    user_id = 2
    user = User(user_id=user_id)
    user_data = user.retrieve_user_data(db_engine)
    return render_template(
        "inbox.html", messages=user_data["messages"], user_id=user_id
    )


@app.route("/inbox/messages")
def messages():
    pass


@app.route("/inbox/message/")
def get_message():
    message = Message(message_id=request.args.get("mesg_id"))
    message = message.retrieve_message(db_engine)
    return render_template("partials/message.html", message=message)


@app.route("/inbox/sent/")
def sent_messages():
    messages = Message(sender_id=request.args.get("user_id"))
    sent_messages = messages.sent_messages(db_engine)
    if isinstance(sent_messages, tuple):
        sent_messages = 0
        print(sent_messages)
    else:
        sent_messages = sent_messages["messages"]
    return render_template("partials/sent.html", messages=sent_messages)


@app.route("/inbox/message/<message_id>", methods=["POST"])
def delete_message():
    pass


@app.route("/inbox/drafts")
def drafts():
    drafts = Message(recipient_id=request.args.get("user_id"))
    drafts = drafts.retrieve_drafts(db_engine)
    print(drafts)
    return render_template(
        "partials/drafts.html", user_id=request.args.get("user_id"), drafts=drafts
    )


@app.route("/inbox/filter")
def sort_filter():
    message = Message(recipient_id=request.args.get("user_id"))
    messages = message.filter_messages(db_engine, request.args.get("sort"))
    return render_template(
        "partials/inbox_filter.html", id=request.args.get("user_id"), messages=messages
    )


@app.route("/inbox/search", methods=["POST"])
def search():
    search = request.form.get("search")
    print(search)
    return f"search: {search}"


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
    current_date = datetime.today()
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
    pass


@app.route("/storage/update", methods=["POST"])
def update_item_name():
    # save change to database and return result
    if request.is_json:
        data = request.get_json()
        print(data)
        return jsonify(data)


@app.route("/storage/add-item/")
def add_storage_item():
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
