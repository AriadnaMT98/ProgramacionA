from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table=True):
     __tablename__ = "movies"

     id: int = Field(primary_key=True)
     nombre_pelicula: str
     anio_estreno: int
     duracion: str
     director: str
     clasificacion: str
     genero: str
