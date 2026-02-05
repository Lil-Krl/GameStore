from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[schemas.UserOut])
def get_all(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/{user_id}", response_model=schemas.UserOut)
def get_one(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user

@router.post("/", response_model=schemas.UserOut, status_code=201)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.put("/{user_id}", response_model=schemas.UserOut)
def update(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(404, "User not found")
    return updated

@router.patch("/{user_id}", response_model=schemas.UserOut)
def patch(user_id: int, user: schemas.UserPatch, db: Session = Depends(get_db)):
    updated = crud.patch_user(db, user_id, user)
    if not updated:
        raise HTTPException(404, "User not found")
    return updated

@router.delete("/{user_id}", status_code=204)
def delete(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(404, "User not found")
