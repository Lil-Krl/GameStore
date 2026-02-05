from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.flush()
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for k, v in user.model_dump().items():
        setattr(db_user, k, v)
    return db_user

def patch_user(db: Session, user_id: int, user: schemas.UserPatch):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for k, v in user.model_dump(exclude_unset=True).items():
        setattr(db_user, k, v)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    return db_user
