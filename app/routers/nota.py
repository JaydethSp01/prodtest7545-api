from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter()

@router.get("/nota", response_model=list[schemas.Nota])
def read_notas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notas = crud.get_notas(db, skip=skip, limit=limit)
    return notas

@router.post("/nota", response_model=schemas.Nota)
def create_nota(nota: schemas.NotaCreate, db: Session = Depends(get_db)):
    return crud.create_nota(db=db, nota=nota)

@router.get("/nota/{nota_id}", response_model=schemas.Nota)
def read_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = crud.get_nota(db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return db_nota

@router.put("/nota/{nota_id}", response_model=schemas.Nota)
def update_nota(nota_id: int, nota: schemas.NotaUpdate, db: Session = Depends(get_db)):
    db_nota = crud.get_nota(db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    return crud.update_nota(db=db, nota=nota, nota_id=nota_id)

@router.delete("/nota/{nota_id}")
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = crud.get_nota(db, nota_id=nota_id)
    if db_nota is None:
        raise HTTPException(status_code=404, detail="Nota not found")
    crud.delete_nota(db=db, nota_id=nota_id)
    return {"ok": True}
