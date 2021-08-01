from typing import List

from fastapi import APIRouter, Depends, Response, status

from ..models.person import StaffOut
from ..models.status import Status, CreateStatus, UpdateStatus
from ..services.auth import get_current_user
from ..services.status import StatusService

router = APIRouter(prefix='/status', tags=['Processing a list of status'])


@router.get('/', response_model=List[Status])
def get_status(service: StatusService = Depends(),
               staff: StaffOut = Depends(get_current_user)):
    return service.get_list()


@router.post('/', response_model=Status)
def create_status(status_name: CreateStatus,
                  service: StatusService = Depends(),
                  staff: StaffOut = Depends(get_current_user)):
    return service.create_status(status_name)


@router.put('/{client_id}', response_model=Status)
def update_status(status_id: int,
                  status_name: UpdateStatus,
                  service: StatusService = Depends(),
                  staff: StaffOut = Depends(get_current_user)):
    return service.update_status_name(status_id, status_name)


@router.delete('/{status_id}')
def delete_status(status_id: int, service: StatusService = Depends(),
                  staff: StaffOut = Depends(get_current_user)):
    service.delete_status(status_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
