from pydantic import BaseModel


class Person(BaseModel):
    name: str
    email: str
    phone: int
    password: str


class Client(Person):
    id: int

    class Config:
        orm_mode = True


class CreateClient(Person):
    pass


class UpdateClient(Person):
    pass
