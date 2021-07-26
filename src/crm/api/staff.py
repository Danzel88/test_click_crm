from typing import List, Optional
from fastapi import Depends, APIRouter, Response, status
from ..services.staff import StaffService
from ..models.staff import Staff, Description, CreateStaff, UpdateStaff

router = APIRouter(prefix="/staff")


@router.get('/', response_model=List[Staff])
def get_staff(service: StaffService = Depends(),
              description: Optional[Description] = None):
    return service.get_list(description=description)


@router.post('/', response_model=Staff)
def create_staff(staff_data: CreateStaff,
                 service: StaffService = Depends()):
    return service.create_staff(staff_data)


@router.put('/{staff_id}', response_model=Staff)
def update_staff(staff_id: int,
                 staff_data: UpdateStaff,
                 service: StaffService = Depends()):
    return service.update_staff(staff_id, staff_data)


@router.delete('/{staff_id}')
def delete_staff(staff_id: int, service: StaffService = Depends()):
    service.delete_staff(staff_id=staff_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
