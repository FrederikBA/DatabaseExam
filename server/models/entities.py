from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    

class Movie(BaseModel):
    movieId: str
    title: str
    rating: float
    summary: str
    actors: list[str]
    directors: list[str]
    genres: list[str]
    publishers: list[str]
    release_year: int
    certificate: str
    runtime: str
    review: list[str]
    poster: str
