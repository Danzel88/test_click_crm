from pydantic import BaseModel


class Person(BaseModel):
    name: str
    email: str
    phone: int
    username: str


class ClientOut(Person):
    id: int
    tg_id: int

    class Config:
        orm_mode = True


class StaffOut(Person):
    id: int

    class Config:
        orm_mode = True


class ClientCreate(Person):
    password: str
    tg_id: int


class StaffCreate(Person):
    password: str


class ClientUpdate(Person):
    tg_id: int


class StaffUpdate(Person):
    password: str