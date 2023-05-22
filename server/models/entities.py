from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    

class Movie(BaseModel):
    poster: str
    movieId: str
    title: str
    summary: str
    runtime: str
    release_year: int
    certificate: str
    rating: float
    genres: list[str]
    publishers: list[str]
    directors: list[str]
    actors: list[str]
    review: list[str]


class MovieSearchRequest(BaseModel):
    query: str