import uuid
from datetime import datetime, timezone
from typing import List, Optional

from email_validator import EmailNotValidError, validate_email
from flask import redirect, url_for
from passlib.hash import pbkdf2_sha256
from sqlmodel import Field, Relationship, Session, SQLModel, select


class User(SQLModel, table=True):
    __tablename__ = "users"
    user_id: int | None = Field(default=None, primary_key=True)
    fullname: str
    email: str = Field(unique=True)
    password: str
    contact_list: List["Contact"] = Relationship(back_populates="user_contacts")
    user_events: List["Event"] = Relationship(back_populates="user_event")
    messages: List["Message"] = Relationship(back_populates="user_message")
    storage: List["Storage"] = Relationship(back_populates="user_storage")

    def register(self, db_engine):
        with Session(db_engine) as session:
            try:
                session.add(self)
                session.commit()
                session.refresh(self)
            except Exception as e:
                session.rollback()
                return f"Unable to save: {e}", 422

    def check_account_existence():
        pass

    def generate_session_id():
        pass


class Profile(SQLModel, table=True):
    __tablename__ = "profiles"
    profile_id: int | None = Field(default=None, primary_key=True)
    mobile: str
    image: str
    status: str = Field(default="available")
    bio: str
    company: str
    city: str
    state: str
    country: str
    user_id: int
    date_added: datetime = Field(default_factory=datetime.utcnow)
    last_active: datetime = Field(default_factory=datetime.utcnow)

    def create_profile(self):
        pass

    def update_profile(self):
        pass


class Contact(SQLModel, table=True):
    __tablename__ = "contacts"
    contact_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id", nullable=False)
    date_added: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="active")  # active, muted or blocked
    fullname: str
    email: str = Field(unique=True)
    company: str
    title: str
    mobile: str
    note: str
    tag: str = Field(index=True)
    user_contacts: User = Relationship(back_populates="contact_list")

    def add_contact(self, db_engine):
        try:
            with Session(db_engine) as session:
                session.add(self)
                session.commit()
                session.rollback(self)
        except Exception as e:
            return f"Unable to save: {e}", 422

    def edit_contact(self, db_engine):
        try:
            with Session(db_engine) as session:
                contact = session.get(Contact, self.contact_id)
                for key, value in self.__dict__.items():
                    if not key.startswith("_") and value is not None:
                        setattr(contact, key, value)
                session.add(contact)
                session.commit()
                session.refresh(contact)
                return contact
        except Exception as e:
            return f"Unable to save: {e}", 422

    def remove_contact(self, db_engine):
        try:
            with Session(db_engine) as session:
                contact = session.exec(
                    select(Contact).where(Contact.contact_id == self.contact_id)
                ).one_or_none()
                session.delete(contact)
                session.commit()
        except Exception as e:
            return f"Unable to delete: {e}", 204

    def contact_list(self, db_engine):
        try:
            with Session(db_engine) as session:
                contacts = session.exec(
                    select(Contact).where(Contact.user_id == self.user_id)
                ).all()
                return [contact for contact in contacts]
        except Exception as e:
            return f"Unable to get contacts:  {e}", 404

    def get_contact(self, db_engine):
        try:
            with Session(db_engine) as session:
                statement = session.exec(
                    select(Contact).where(Contact.contact_id == self.contact_id)
                )
                contact = statement.first().dict()
                return contact
        except Exception as e:
            return f"Unable to find contact: {e}", 404


class Event(SQLModel, table=True):
    __tablename__ = "events"
    event_id: int | None = Field(default=None, primary_key=True)
    event_name: str
    venue: str
    event_datetime: datetime
    category: str  # work, social, family, vacation
    priority: str = Field(default="normal")  # normal or high
    note: str
    user_id: int = Field(foreign_key="users.user_id", nullable=False)
    user_event: User = Relationship(back_populates="user_events")

    def retrieve_events(self, db_engine):
        try:
            with Session(db_engine) as session:
                events = session.exec(
                    select(Event).where(Event.user_id == self.user_id)
                ).all()
                return [event for event in events]
        except Exception as e:
            return f"Unable to retrieve events: {e}", 404

    def retrieve_event(self, db_engine):
        try:
            with Session(db_engine) as session:
                result = session.exec(
                    select(Event).where(Event.event_id == self.event_id)
                )
                event = result.first().dict()
                return event
        except Exception as e:
            return f"Unable to retrieve event: {e}", 404

    def add_event(self, db_engine):
        try:
            with Session(db_engine) as session:
                session.add(self)
                session.commit()
                session.rollback(self)
        except Exception as e:
            return f"Unable to save event: {e}", 422

    def cancel_event(self, db_engine):
        try:
            with Session(db_engine) as session:
                result = session.exec(
                    select(Event).where(Event.event_id == self.event_id)
                ).one()
                session.delete(result)
                session.commit()
        except Exception as e:
            return f"Unable to remove event: {e}", 404

    def edit_event(self, db_engine):
        try:
            with Session(db_engine) as session:
                event = session.get(Event, self.event_id)
                for key, value in self.__dict__.items():
                    if not key.startswith("_") and value is not None:
                        setattr(event, key, value)
                session.add(event)
                session.commit()
                session.refresh(event)
                return event
        except Exception as e:
            return f"Unable to update event: {e}", 422

    def send_notification(self):
        pass


class Message(SQLModel, table=True):
    __tablename__ = "messages"
    message_id: int | None = Field(default=None, primary_key=True)
    sender_id: int = Field(foreign_key="users.user_id")
    recipient_id: int
    subject: str
    body: str
    message_type: str = Field(default="message")  # draft or message
    message_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="unread")
    user_message: User = Relationship(back_populates="messages")

    def send_message():
        pass

    def delete_message():
        pass

    def retrieve_message():
        pass

    def retrieve_all_messages():
        pass

    def retrieve_drafts():
        pass

    def retrieve_draft():
        pass

    def mark_as_draft():
        pass

    def filter_messages():
        pass


class Storage(SQLModel, table=True):
    storage_item_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    item_name: str
    item_type: str
    item_size: int
    date_added: datetime = Field(default_factory=datetime.utcnow)
    user_storage: User = Relationship(back_populates="storage")

    def add_item(self, db_engine):
        try:
            with Session(db_engine) as session:
                session.add(self)
                session.commit()
                session.rollback(self)
        except Exception as e:
            return f"Unable to save storage item: {e}", 422

    def remove_item():
        pass

    def edit_item(self, db_engine):
        try:
            with Session(db_engine) as session:
                result = session.get(Storage, self.storage_item_id)
                for key, value in self.__dict__.items():
                    if not key.startswith("_") and value is not None:
                        setattr(result, key, value)
                session.add(result)
                session.commit()
                session.refresh(result)
                return result
        except Exception as e:
            return f"Unable to update: {e}", 422

    def retrieve_item():
        pass

    def retrieve_items():
        pass

    def item_filter():
        pass

    def disk_usage():
        # a user gets 2GB
        pass

    def disk_analyzer():
        # looks at the file formats saved to your disk space(images, audio files etc)
        # and returns the number of files in that format and percentage saved of that file type
        pass


class Security:
    def __init__(self):
        self.attempts = 0
        self.ip_addresses = []
        self.blacklisted = []
        self.special_characters = r"1234567890~</>(-)+=\\'&^%$#@,?!*|[{]}:;"

    def validate_name(self, fullname):
        for special_character in self.special_characters:
            for letter in fullname:
                if letter == special_character:
                    return "Invalid name"
        return fullname

    def whitespace_formatter(self, field):
        """Ensure that there is only one space character"""
        pass

    def validate_email(self, user_email):
        try:
            email = validate_email(user_email, check_deliverability=False)
            return email.normalized
        except EmailNotValidError as e:
            return f"Invalid email: {e}"

    def _hash_password(self, password):
        return pbkdf2_sha256.hash(password)

    def _check_password_length(self, password):
        if len(password) < 8:
            return "Password is too short", 401
        security = Security()
        return security._hash_password(password)

    def validate_password(self, password):
        security = Security()
        return security._check_password_length(password)

    def reset_password(self):
        pass

    def validate_mobile(self, mobile):
        if not mobile.isdigit() or len(mobile) > 15:
            return "Please provide no more than 15 characters, digits only", 422
        else:
            return mobile

    def validate_fields(fields):
        pass

    def rate_limit(self, current_user_ip, current_page):
        self.attempts += 1
        if len(self.ip_addresses) == 0:
            self.ip_addresses.append(current_user_ip)
        else:
            for ip_address in self.ip_addresses:
                if current_user_ip != ip_address:
                    self.ip_addresses.append(current_user_ip)
                if current_user_ip == ip_address and self.attempts < 3:
                    return redirect(url_for(current_page))
                if self.attempts > 2:
                    # log IP and blacklist it and require account verification
                    Security._blacklist_ip(self, current_user_ip)
                    return redirect(
                        url_for(
                            current_page,
                            message="Too many attempts, you will need to verify your account click here",
                        )
                    )

    def _blacklist_ip(self, ip):
        self.blacklisted.append(ip)
        # save to a database of blocked IP addresses

    def verify_account():
        pass

    def compare_passwords():
        pass
