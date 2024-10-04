from pydantic import BaseModel

class Nationalities(BaseModel):
    id: int
    abreviacion: str
    descripcion: str
    
    class Config:
        orm_mode = True