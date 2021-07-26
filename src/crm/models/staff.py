from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Description(str, Enum):
    MECHANIC = 'mech'
    DRIVER = 'driver'
    ELECTRIC = "electric"


class Person(BaseModel):
    name: str
    description: Optional[str]
    email: str
    phone: int
    password: str


class Staff(Person):
    id: int

    class Config:
        orm_mode = True


class CreateStaff(Person):
    pass


class UpdateStaff(Person):
    pass



