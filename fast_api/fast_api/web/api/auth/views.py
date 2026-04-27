from fastapi import APIRouter, Depends, HTTPException
from fast_api.db.dao.user_dao import UserDAO
from fast_api.web.api.auth.schema import UserCreate
from fast_api.services.jwt import create_access_token, get_current_user

router = APIRouter()


@router.post("/signup")
async def signup(user_data: UserCreate, dao: UserDAO = Depends()) -> dict:
    existing = await dao.get_by_email(user_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    await dao.create_user(user_data.email, user_data.password)
    return {"message": "User created successfully"}


@router.post("/login")
async def login(user_data: UserCreate, dao: UserDAO = Depends()) -> dict:
    user = await dao.get_by_email(user_data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    if not dao.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    token = create_access_token(user.email)
    return {"access_token": token, "token_type": "bearer"}
