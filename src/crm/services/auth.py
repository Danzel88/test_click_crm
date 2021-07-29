from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.hash import bcrypt
from fastapi import status, HTTPException, Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session


from .. import tables
from ..database import get_session
from ..models.person import StaffCreate, StaffOut
from ..models.auth import Token
from ..settings import setting


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')


def get_current_user(token: str = Depends(oauth2_scheme)) -> StaffOut:
    return AuthService.validate_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, raw_password: str, hash_password: str) -> bool:
        return bcrypt.verify(raw_password, hash_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> StaffOut:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Validate credential failed",
            headers={'WWW-Authenticate': 'Bearer'}
        )
        try:
            payload = jwt.decode(token, setting.jwt_secret,
                                 algorithms=[setting.jwt_algorithm])
            print(payload)
        except JWTError:
            raise exception from None

        staff_data = payload.get("staff")
        try:
            staff = StaffOut.parse_obj(staff_data)
        except ValidationError:
            raise exception from None

        return staff

    @classmethod
    def create_token(cls, staff: tables.Staff) -> Token:
        staff_data = StaffOut.from_orm(staff)

        now = datetime.utcnow()
        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(seconds=3600),
            "sub": str(staff_data.id),
            "staff": staff_data.dict()
        }
        token = jwt.encode(
            payload,
            setting.jwt_secret,
            algorithm=setting.jwt_algorithm
        )

        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_staff(self, staff_data: StaffCreate) -> Token:
        staff = tables.Staff(
            name=staff_data.name,
            username=staff_data.username,
            email=staff_data.email,
            phone=staff_data.phone,
            password_hash=self.hash_password(staff_data.password)
        )

        self.session.add(staff)
        self.session.commit()

        return self.create_token(staff)

    def authenticate_staff(self, username: str, password: str) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        staff = (self.session.query(tables.Staff).filter(tables.Staff.username == username).first())

        if not staff:
            raise exception

        if not self.verify_password(password, staff.password_hash):
            print("NOR VERIFY")
            raise exception

        return self.create_token(staff)
