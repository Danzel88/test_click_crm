from typing import List
from fastapi import Depends, APIRouter, Response, status
from ..services.client import ClientService
from ..models.client import Client, CreateClient, UpdateClient

router = APIRouter(prefix="/client")


@router.get('/', response_model=List[Client])
def get_client(service: ClientService = Depends()):
    return service.get_list()


@router.post('/', response_model=Client)
def create_client(client_data: CreateClient, service: ClientService = Depends()):
    return service.create_client(client_data)


@router.put('/{client_id}', response_model=Client)
def update_client(client_id: int,
                  client_data: UpdateClient,
                  service: ClientService = Depends()):
    return service.update_client(client_id, client_data)


@router.delete('/{client_id}')
def delete_client(client_id: int, service: ClientService = Depends()):
    service.delete_client(client_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
