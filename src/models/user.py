from sqlalchemy import Table, Column,  String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from ..config.database import meta, engine
import datetime
import uuid

# user model using sqlalchemy

def generate_uuid():
    return str(uuid.uuid4())  

users = Table("user", meta,
             Column("id", String(50), primary_key=True, default=generate_uuid),
             Column("username", String(50), unique=True),
             Column("password", String(256)),
             Column("email", String(50), unique=True),
             Column("created_at", DateTime, default=datetime.datetime.now))

meta.create_all(engine)   