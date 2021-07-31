from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from ..models.person import StaffCreate, StaffOut
from ..models.auth import Token
from ..services.auth import AuthService, get_current_user

router = APIRouter(prefix='/auth', tags=['Authenticate'])


@router.post('/sign-up', response_model=Token,
             status_code=status.HTTP_201_CREATED)
def sign_up(staff_data: StaffCreate, service: AuthService = Depends()):
    return service.register_new_staff(staff_data)


@router.post('/sign-in', response_model=Token)
def sign_in(form_data: OAuth2PasswordRequestForm = Depends(),
            service: AuthService = Depends()):
    return service.authenticate_staff(form_data.username,
                                      form_data.password)


@router.get('/user/', response_model=StaffOut)
def get_user(staff: StaffOut = Depends(get_current_user)):
    return staff
