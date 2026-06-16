from pydantic import BaseModel
class Nota(BaseModel):
    id: int
    title: str
    category: str
    user: str
class Categoria(BaseModel):
    id: int
    name: str
class Usuario(BaseModel):
    id: int
    name: str
