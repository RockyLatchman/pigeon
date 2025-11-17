import uuid
from datetime import datetime, timezone
from typing import List, Optional

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
                print(f"Error creating a {e}")


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

    def check_account_existence():
        pass

    def validate_email():
        pass

    def compare_passwords():
        pass

    def generate_session_id():
        pass


class Contact(SQLModel, table=True):
    __tablename__ = "contacts"
    contact_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id", nullable=False)
    date_added: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="active")  # active, muted or blocked
    user_contacts: User = Relationship(back_populates="contact_list")

    def add_contact():
        pass

    def block_contact():
        pass

    def remove_contact():
        pass

    def edit_contact():
        pass

    def contact_list():
        pass

    def get_contact():
        pass

    def filter_contacts():
        pass


class Event(SQLModel, table=True):
    __tablename__ = "events"
    event_id: int | None = Field(default=None, primary_key=True)
    event_name: str
    venue: str
    event_datetime: datetime = Field(default_factory=datetime.utcnow)
    category: str  # work, social, family, vacation
    priority: str = Field(default="normal")  # normal or high
    user_id: int = Field(foreign_key="users.user_id", nullable=False)
    user_event: User = Relationship(back_populates="user_events")

    def retrieve_events():
        pass

    def retrieve_event():
        pass

    def add_event():
        pass

    def cancel_event():
        pass

    def edit_event():
        pass

    def send_invite():
        pass

    def filter_events():
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

    def add_item():
        pass

    def remove_item():
        pass

    def edit_item():
        pass

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
    def validate_email():
        pass

    @classmethod
    def hash_password(cls, password):
        return pbkdf2_sha256.hash(password)

    def _check_password_length(password):
        if len(password) < 8:
            return "Password is too short"
        return password

    def validate_password():
        pass

    def validate_fields(fields):
        pass

    def rate_limit(self, attempts):
        pass
