from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/categoria", tags=["categorias"])

@router.get("/", response_model=list[schemas.Categoria])
def read_categorias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categorias = db.query(models.Categoria).offset(skip).limit(limit).all()
    return categorias

@router.post("/", response_model=schemas.Categoria)
def create_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = models.Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.get("/{categoria_id}", response_model=schemas.Categoria)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return categoria

@router.put("/{categoria_id}", response_model=schemas.Categoria)
def update_categoria(categoria_id: int, categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    for key, value in categoria.dict().items():
        setattr(db_categoria, key, value)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.delete("/{categoria_id}", response_model=schemas.Categoria)
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    db.delete(categoria)
    db.commit()
    return categoria;