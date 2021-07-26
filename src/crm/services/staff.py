from typing import List, Optional

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .. import tables
from ..database import get_session
from ..models.staff import Description, CreateStaff, UpdateStaff


class StaffService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, staff_id) -> tables.Staff:
        staff = self.session.query(tables.Staff).filter_by(id=staff_id).first()
        if not staff:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return staff

    def get_list(self, description: Optional[Description] = None) \
            -> List[tables.Staff]:
        query = self.session.query(tables.Staff)
        if description:
            query = query.filter_by(description=description)
        staff = query.all()
        return staff

    def create_staff(self, staff_data: CreateStaff) -> tables.Staff:
        staff = tables.Staff(**staff_data.dict())
        self.session.add(staff)
        self.session.commit()
        return staff

    def update_staff(self, staff_id: int, staff_data: UpdateStaff) \
            -> tables.Staff:
        staff = self._get(staff_id)
        for field, value in staff_data:
            setattr(staff, field, value)
        self.session.commit()
        return staff

    def delete_staff(self, staff_id: int):
        staff = self._get(staff_id)
        self.session.delete(staff)
        self.session.commit()

