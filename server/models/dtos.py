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
    
class priceDTO(BaseModel):
    title: str
    price: float

class sortDTO(BaseModel):
    sort_value: str
    sort_order: str

class registerDTO(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str