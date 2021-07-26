from typing import List, Optional
from fastapi import Depends, APIRouter, Response, status
from ..services.client_request import ClientRequestService
from ..models.client_request import ClientRequest, UpdateClientRequest, CreateClientRequest

router = APIRouter(prefix="/client_request")


@router.get('/', response_model=List[ClientRequest])
def get_client_request(service: ClientRequestService = Depends()):
    return service.get_list()


@router.post('/', response_model=ClientRequest)
def create_client_request(request_data: CreateClientRequest, service: ClientRequestService =
                          Depends()):
    return service.create_client_request(request_data)


@router.put('/{client_request_id}', response_model=ClientRequest)
def update_client_request(client_request_id: int,
                          request_data: UpdateClientRequest,
                          service: ClientRequestService =
                          Depends()):
    return service.update_client_request(client_request_id, request_data)


@router.delete('/{client_request_id}')
def delete_client_request(client_request_id: int,
                          service: ClientRequestService = Depends()):
    service.delete_client_request(client_request_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
