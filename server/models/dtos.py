from pydantic import BaseModel

class cartDTO(BaseModel):
    user_id: int
    movie_id: str