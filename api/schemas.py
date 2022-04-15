from pydantic import BaseModel


class Prints(BaseModel):
    id = int
    key = str
    author = str
    details = str
    blueprint = str
    created_at = str
    updated_at = str
    favorites = str
    # image = str

    class Config:
        orm_mode = True

