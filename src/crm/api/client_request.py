from datetime import datetime
from typing import List, Optional
from fastapi import Depends, APIRouter, Response, status

from ..models.person import StaffOut
from ..services.auth import get_current_user
from ..services.client_request import ClientRequestService

from ..models.client_request import (ClientRequest,
                                     UpdateClientRequest,
                                     CreateClientRequest)

router = APIRouter(prefix="/client_request",
                   tags=['Processing requests of clients'])


@router.get('/', response_model=List[ClientRequest])
def get_client_request(service: ClientRequestService = Depends(),
                       staff: StaffOut = Depends(get_current_user),
                       status_request: Optional[str] = None,
                       type_request: Optional[str] = None,
                       start_date: Optional[str] = None,
                       end_date: Optional[str] = None
                       ):
    return service.get_list(status_request, type_request, start_date, end_date)


@router.post('/', response_model=ClientRequest)
def create_client_request(request_data: CreateClientRequest,
                          service: ClientRequestService = Depends(),
                          staff: StaffOut = Depends(get_current_user)):
    return service.create_client_request(request_data)


@router.put('/{client_request_id}', response_model=ClientRequest)
def update_client_request(client_request_id: int,
                          request_data: UpdateClientRequest,
                          service: ClientRequestService =
                          Depends(),
                          staff: StaffOut = Depends(get_current_user)):
    return service.update_client_request(client_request_id, request_data)


@router.delete('/{client_request_id}')
def delete_client_request(client_request_id: int,
                          service: ClientRequestService = Depends(),
                          staff: StaffOut = Depends(get_current_user)):
    service.delete_client_request(client_request_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
