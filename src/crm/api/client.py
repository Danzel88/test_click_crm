from typing import List
from fastapi import Depends, APIRouter, Response, status

from ..models.person import ClientOut, ClientUpdate, ClientCreate
from ..services.client import ClientService

router = APIRouter(prefix="/client")


@router.get('/', response_model=List[ClientOut])
def get_client(service: ClientService = Depends()):
    return service.get_list()


@router.post('/', response_model=ClientOut)
def create_client(client_data: ClientCreate, service: ClientService = Depends()):
    return service.create_client(client_data)


@router.put('/{client_id}', response_model=ClientOut)
def update_client(client_id: int,
                  client_data: ClientUpdate,
                  service: ClientService = Depends()):
    return service.update_client(client_id, client_data)


@router.delete('/{client_id}')
def delete_client(client_id: int, service: ClientService = Depends()):
    service.delete_client(client_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
