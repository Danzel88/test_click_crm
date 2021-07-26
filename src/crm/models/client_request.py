from pydantic import BaseModel
from datetime import date


class BaseClientRequests(BaseModel):
    date_request: date
    subject: str
    type_request_id: int
    status_id: int
    client_id: int


class ClientRequest(BaseClientRequests):
    id: int

    class Config:
        orm_mode = True


class CreateClientRequest(BaseClientRequests):
    pass


class UpdateClientRequest(BaseClientRequests):
    pass
