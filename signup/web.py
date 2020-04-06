import logging

from fastapi import Depends, FastAPI, Header, HTTPException, status
from pydantic import BaseModel, EmailStr
from fastapi.security import OAuth2PasswordBearer

from .utilities import check_auth_header

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


class Signup(BaseModel):
    timestamp: str
    email: EmailStr
    name: str
    comments: str


def make_app():
    app = FastAPI()
    @app.get("/")
    async def index():
        return {'hi': 'there'}

    @app.post("/signup")
    async def signup(*, data: Signup, authorization: str = Header('Basic ')):
        if not check_auth_header(authorization):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return {'success': True}
    return app

