from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from .. import tables
from ..database import get_session
from ..models.person import ClientCreate, ClientUpdate


class ClientService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, client_id: int) -> tables.Client:
        client = self.session.query(tables.Client).filter_by(id=client_id).first()
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return client

    def get_list(self) -> List[tables.Client]:
        clients = (self.session.query(tables.Client).all())
        return clients

    def create_client(self, client_data: ClientCreate) -> tables.Client:
        client = tables.Client(**client_data.dict())
        self.session.add(client)
        self.session.commit()
        return client

    def update_client(self, client_id: int, client_data: ClientUpdate) -> tables.Client:
        client = self._get(client_id)
        for field, value in client_data:
            setattr(client, field, value)
        self.session.commit()
        return client

    def delete_client(self, client_id: int):
        client = self._get(client_id)
        self.session.delete(client)
        self.session.commit()

