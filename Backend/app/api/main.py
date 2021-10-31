from fastapi import APIRouter, Body, Depends, Path, Query

router = APIRouter()


@router.get("/")
def root():
    return {message: "welcome to Drive(h)er"}

# @router.post("")
