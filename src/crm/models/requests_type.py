from pydantic import BaseModel


class BaseRequestsType(BaseModel):
    name: str


class RequestsType(BaseRequestsType):
    id: int

    class Config:
        orm_mode = True


class CreateRequestsType(BaseRequestsType):
    pass


class UpdateRequestsType(BaseRequestsType):
    pass


class GetRt(BaseModel):
    requests_type_name: str