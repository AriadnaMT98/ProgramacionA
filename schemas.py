from pydantic import BaseModel

class MoviesSchema(BaseModel):
    nombre_pelicula: str
    anio_estreno: int
    duracion: str
    director: str
    clasificacion: str
    genero: str