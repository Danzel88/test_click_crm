from typing import List

from fastapi import APIRouter, Depends, Response, status

from ..models.person import StaffOut
from ..models.requests_type import RequestsType, CreateRequestsType, UpdateRequestsType
from ..services.auth import get_current_user
from ..services.requests_type import RequestsTypeService

router = APIRouter(prefix='/requests_type', tags=['Processing a list of request types'])


@router.get('/', response_model=List[RequestsType])
def get_request_type(service: RequestsTypeService = Depends(),
                     staff: StaffOut = Depends(get_current_user)):
    return service.get_list()


@router.post('/', response_model=RequestsType)
def create_request_type(request_type_name: CreateRequestsType,
                        service: RequestsTypeService = Depends(),
                        staff: StaffOut = Depends(get_current_user)):
    return service.create_requests_type(request_type_name)


@router.put('/{requests_type_id}', response_model=RequestsType)
def update_request_type(requests_type_id: int,
                        request_type: UpdateRequestsType,
                        service: RequestsTypeService = Depends(),
                        staff: StaffOut = Depends(get_current_user)):
    return service.update_requests_type(requests_type_id, request_type)


@router.delete('/{requests_type_id}')
def delete_requests_type(request_type_id: int, service: RequestsTypeService
                         = Depends(), staff: StaffOut = Depends(get_current_user)):
    service.delete_requests_type(request_type_id=request_type_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
