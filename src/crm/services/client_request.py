from datetime import datetime
from typing import List, Optional
from icecream import ic
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import ArgumentError, DataError
from sqlalchemy.orm import Session
from crm import tables
from crm.database import get_session
from crm.models.client_request import UpdateClientRequest, CreateClientRequest


class ClientRequestService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, client_request_id: int) -> tables.ClientRequests:
        client_request_id = self.session.query(tables.ClientRequests) \
            .filter_by(id=client_request_id).first()
        if not client_request_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return client_request_id

    def _filter_by_date(self, start_date: Optional[str] = None,
                        end_date: Optional[str] = None):
        exception = HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The date must be in the format YYY-MM-DD")
        try:
            sd = datetime.strptime(start_date, '%Y-%m-%d')
            ed = datetime.strptime(end_date, '%Y-%m-%d')
        except (ValueError, TypeError):
            raise exception
        if start_date and end_date:
            query = self.session.query(tables.ClientRequests) \
                .order_by(tables.ClientRequests.date_request) \
                .filter(tables.ClientRequests.date_request >= sd) \
                .filter(tables.ClientRequests.date_request <= ed)
        elif not start_date:
            query = self.session.query(tables.ClientRequests) \
                .order_by(tables.ClientRequests.date_request) \
                .filter(tables.ClientRequests.date_request <= ed)
        elif not end_date:
            query = self.session.query(tables.ClientRequests) \
                .order_by(tables.ClientRequests.date_request) \
                .filter(tables.ClientRequests.date_request >= sd)
        return query

    def _type_and_status_filter(self, status_name: Optional[str] = None,
                                type_request_name: Optional[str] = None):
        status_id = [i[0] for i in self.session.query(tables.Status.id) \
            .filter_by(name=status_name)]
        type_request_id = [i[0] for i in
                           self.session.query(tables.RequestsType.id) \
                               .filter_by(name=type_request_name)]
        if status_id:
            query = self.session.query(tables.ClientRequests) \
                .filter_by(status_id=status_id[0])
        elif type_request_id:
            query = self.session.query(tables.ClientRequests) \
                .filter_by(type_request_id=type_request_id[0])
        elif status_id and type_request_id:
            query = self.session.query(tables.ClientRequests) \
                .filter_by(status_id_id=status_id[0])\
                .filter_by(type_request_id=type_request_id[0])
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return query

    def get_list(self, status_request: Optional[str] = None,
                 type_request: Optional[str] = None,
                 start_date: Optional[str] = None,
                 end_date: Optional[str] = None) -> List:
        query = self.session.query(tables.ClientRequests) \
            .order_by(tables.ClientRequests.date_request)
        if status_request:
            query = self._type_and_status_filter(status_name=status_request)
        if type_request:
            query = self._type_and_status_filter(type_request_name=type_request)
        if start_date or end_date:
            query = self._filter_by_date(start_date=start_date, end_date=end_date)
        client_request = query.all()
        return client_request

    def create_client_request(self, client_data: CreateClientRequest) \
            -> tables.ClientRequests:
        client_request = tables.ClientRequests(**client_data.dict())
        self.session.add(client_request)
        self.session.commit()
        return client_request

    def update_client_request(self, client_request_id: int,
                              client_request_data: UpdateClientRequest) \
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
