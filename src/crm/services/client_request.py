from enum import Enum
from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from crm import tables
from crm.database import get_session
from crm.models.client_request import UpdateClientRequest, CreateClientRequest


class ClientRequestService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, client_request_id: int) -> tables.ClientRequests:
        client_request_id = self.session.query(tables.ClientRequests)\
            .filter_by(id=client_request_id).first()
        if not client_request_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return client_request_id

    def get_list(self) -> List[tables.ClientRequests]:
        query = self.session.query(tables.ClientRequests)
        client_request = query.all()
        return client_request

    def create_client_request(self, client_data: CreateClientRequest)\
            -> tables.ClientRequests:
        client_request = tables.ClientRequests(**client_data.dict())
        self.session.add(client_request)
        self.session.commit()
        return client_request

    def update_client_request(self, client_request_id: int, client_request_data: UpdateClientRequest)\
            -> tables.ClientRequests:
        client_request = self._get(client_request_id)
        for field, value in client_request_data:
            setattr(client_request, field, value)
        self.session.commit()
        return client_request

    def delete_client_request(self, client_request_id: int):
        client_request = self._get(client_request_id)
        self.session.delete(client_request)
        self.session.commit()