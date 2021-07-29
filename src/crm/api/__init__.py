from fastapi import APIRouter
from .staff import router as staff_router
from .client import router as client_router
from .client_request import router as client_request_router
from .status import router as status_router
from .requests_type import router as rtr
from .auth import router as auth_router


router = APIRouter()

router.include_router(auth_router)
router.include_router(staff_router)
router.include_router(client_router)
router.include_router(client_request_router)
router.include_router(status_router)
router.include_router(rtr)

