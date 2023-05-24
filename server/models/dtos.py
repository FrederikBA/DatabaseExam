from pydantic import BaseModel

class cartDTO(BaseModel):
    user_id: int
    movie_id: str

class MovieDTO(BaseModel):
    movie_id: str


class orderDTO(BaseModel):
    movies: list[MovieDTO]
    member_id: str
    total_price: float