from pydantic import BaseModel
class User(BaseModel):
    id:int
    title: str
    description: str
    completed: bool