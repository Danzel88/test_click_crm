from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .. import tables
from ..database import get_session
from ..models.person import StaffUpdate


class StaffService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, staff_id) -> tables.Staff:
        staff = self.session.query(tables.Staff).filter_by(id=staff_id).first()
        if not staff:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return staff

    def get_list(self) -> List[tables.Staff]:
        query = self.session.query(tables.Staff)
        staff = query.all()
        return staff

    def update_staff(self, staff_id: int, staff_data: StaffUpdate) -> tables.Staff:
        staff = self._get(staff_id)
        for field, value in staff_data:
            setattr(staff, field, value)
        self.session.commit()
        return staff

    def delete_staff(self, staff_id: int):
        staff = self._get(staff_id)
        self.session.delete(staff)
        self.session.commit()

