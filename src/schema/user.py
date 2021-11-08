
from pydantic import BaseModel, UUID4
from typing import Optional, Union
import datetime
from uuid import UUID
# from sqlalchemy.dialects.postgresql import UUID


class User(BaseModel):
    id: Optional[str]
    username: str
    password: str
    email: str
    created_at: Optional[datetime.datetime]
