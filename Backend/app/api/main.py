from fastapi import APIRouter, Body, Depends, Path, Query, Response, status
from fastapi.security import HTTPBearer

router = APIRouter()


@router.get("/")
def root():
    return {message: "welcome to Drive(h)er"}

# @router.post("")
