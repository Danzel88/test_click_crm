from typing import List

from fastapi import Depends, HTTPException, status
from .. import tables
from ..database import get_session
from sqlalchemy.orm import Session
from ..models.requests_type import CreateRequestsType, UpdateRequestsType


class RequestsTypeService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, requests_type_id) -> tables.RequestsType:
        requests_type = self.session.query(tables.RequestsType)\
            .filter_by(id=requests_type_id).first()
        if not requests_type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return requests_type

    def get_list(self) -> List[tables.RequestsType]:
        all_request_type = (self.session.query(tables.RequestsType).all())
        return all_request_type

    def create_requests_type(self, requests_type_name: CreateRequestsType)\
            -> tables.RequestsType:
        requests_type = tables.RequestsType(**requests_type_name.dict())
        self.session.add(requests_type)
        self.session.commit()
        return requests_type

    def update_requests_type(self, requests_type_id: int, new_requests_type: UpdateRequestsType)\
            -> tables.RequestsType:
        requests_type = self._get(requests_type_id)
        for key, value in new_requests_type:
            setattr(requests_type, key, value)
        self.session.commit()
        return requests_type

    def delete_requests_type(self, request_type_id: int):
        request_type = self._get(request_type_id)
        self.session.delete(request_type)
        self.session.commit()
