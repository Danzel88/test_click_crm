from typing import List
from fastapi import Depends, APIRouter, Response, status

from ..models.person import StaffUpdate
from ..services.auth import get_current_user
from ..services.staff import StaffService
from ..models.person import StaffOut


router = APIRouter(prefix="/staff",
                   tags=['Receiving, update and deleting employee entity'])


@router.get('/', response_model=List[StaffOut])
def get_staff(service: StaffService = Depends()):
    return service.get_list()


@router.put('/{staff_id}', response_model=StaffOut)
def update_staff(staff_id: int,
                 staff_data: StaffUpdate,
                 service: StaffService = Depends(),
                 staff: StaffOut = Depends(get_current_user)):
    return service.update_staff(staff_id, staff_data)


@router.delete('/{staff_id}')
def delete_staff(staff_id: int, service: StaffService = Depends(),
                 staff: StaffOut = Depends(get_current_user)):
    service.delete_staff(staff_id=staff_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
