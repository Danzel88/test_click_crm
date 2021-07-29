from pydantic import BaseModel


class BaseStatus(BaseModel):
    name: str


class Status(BaseStatus):
    id: int

    class Config:
        orm_mode = True


class CreateStatus(BaseStatus):
    pass


class UpdateStatus(BaseStatus):
    pass


class GetStatus(BaseStatus):
    status_name: str