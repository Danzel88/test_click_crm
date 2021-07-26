from typing import List

from fastapi import Depends, HTTPException, status
from .. import tables
from ..database import get_session
from sqlalchemy.orm import Session

from ..models.status import CreateStatus, UpdateStatus


class StatusService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, status_id) -> tables.Status:
        statuses = self.session.query(tables.Status).filter_by(id=status_id).first()
        if not status:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return statuses

    def get_list(self) -> List[tables.Status]:
        all_status = (self.session.query(tables.Status).all())
        return all_status

    def create_status(self, status_name: CreateStatus) -> tables.Status:
        s = tables.Status(**status_name.dict())
        self.session.add(s)
        self.session.commit()
        return s

    def update_status_name(self, status_id: int, new_status_name: UpdateStatus) -> tables.Status:
        updated_status = self._get(status_id)
        for key, value in new_status_name:
            setattr(updated_status, key, value)
        self.session.commit()
        return updated_status

    def delete_status(self, status_id: int):
        status = self._get(status_id)
        self.session.delete(status)
        self.session.commit()
