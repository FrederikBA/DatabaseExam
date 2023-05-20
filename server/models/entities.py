from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    
class Movie(BaseModel):

    title: str
    
    
    #remember to add these to the movie
    #poster, title,genre, release_year,runtime, summary, director, actors,
