from typing import List
from passlib.hash import bcrypt
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .. import tables
from ..database import get_session
from ..models.person import StaffUpdate


class StaffService:
    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

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
        staff.name = staff_data.name
        staff.email = staff_data.email
        staff.phone = staff_data.phone
        staff.username = staff_data.username
        staff.password_hash = self.hash_password(staff_data.password)
        self.session.commit()
        return staff

    def delete_staff(self, staff_id: int):
        staff = self._get(staff_id)
        self.session.delete(staff)
        self.session.commit()

